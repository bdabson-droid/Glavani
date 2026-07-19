import staticFormsPlugin from "@cloudflare/pages-plugin-static-forms";

const BOOKING_FORM = "glavani-booking";
const CONTACT_FORM = "glavani-contact";

interface Env {
  RESEND_API_KEY?: string;
  RESEND_FROM_EMAIL?: string;
  RESEND_BOOKING_FROM_EMAIL?: string;
  RESEND_CONTACT_FROM_EMAIL?: string;
  RESEND_TO_EMAIL?: string;
}

const DEFAULT_BOOKING_FROM_EMAIL = "booking@glavani-park.com";
const DEFAULT_CONTACT_FROM_EMAIL = "contact@glavani-park.com";
const DEFAULT_TO_EMAIL = "info@glavanipark.com";

function field(formData: FormData, key: string): string {
  const value = formData.get(key);
  return value == null ? "" : String(value).trim();
}

function containsLink(value: string): boolean {
  const text = value.trim();
  if (!text) return false;
  if (/https?:\/\//i.test(text)) return true;
  if (/\bwww\./i.test(text)) return true;
  if (/<a\s[\s\S]*?href\s*=/i.test(text)) return true;
  if (/\[[\s\S]*?\]\(\s*https?:/i.test(text)) return true;
  if (
    /\b[a-z0-9][-a-z0-9]{0,62}\.(com|net|org|io|co|uk|de|hr|info|biz|xyz|ru|cn|tk|click|link|top|shop|site|online|me|ly)(?:\/[^\s]*)?\b/i.test(
      text,
    )
  ) {
    return true;
  }
  return false;
}

function contactFormContainsLink(formData: FormData): boolean {
  return ["message", "name", "activity"].some((key) =>
    containsLink(field(formData, key)),
  );
}

function replyToLine(guestName: string, guestEmail: string): string {
  if (!guestEmail) return "Reply to confirm: (no email provided)";
  const who = guestName ? `${guestName} <${guestEmail}>` : guestEmail;
  return `Reply to confirm: ${who}`;
}

function formatBookingDate(raw: string, lang: string): string {
  const trimmed = raw.trim();
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(trimmed);
  if (!match) return trimmed || "date TBC";
  const year = Number(match[1]);
  const month = Number(match[2]);
  const day = Number(match[3]);
  const date = new Date(Date.UTC(year, month - 1, day));
  const locale = lang === "hr" ? "hr-HR" : "en-GB";
  return new Intl.DateTimeFormat(locale, {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  }).format(date);
}

function buildBookingEmailBody(
  formData: FormData,
  guestName: string,
  guestEmail: string,
): string {
  const message = field(formData, "message");
  if (message) {
    return [replyToLine(guestName, guestEmail), "", message].join("\n");
  }

  return [
    replyToLine(guestName, guestEmail),
    "",
    field(formData, "header") || "Glavani Park booking request",
    "---",
    `Package: ${field(formData, "package")}`,
    `Date: ${formatBookingDate(field(formData, "date"), field(formData, "lang"))}`,
    `Arrival: ${field(formData, "arrival")}`,
    `Guests: ${field(formData, "guests")}`,
    `Adults: ${field(formData, "adults")}`,
    `Children: ${field(formData, "children")}`,
    `Total: ${field(formData, "total")}`,
    `Name: ${guestName}`,
    `Email: ${guestEmail}`,
    `Phone: ${field(formData, "phone")}`,
    `Notes: ${field(formData, "notes") || "—"}`,
    "---",
    "Glavani Park · Glavani 10, Barban, Istria",
  ].join("\n");
}

function buildContactEmailBody(
  formData: FormData,
  guestName: string,
  guestEmail: string,
): string {
  return [
    replyToLine(guestName, guestEmail),
    "",
    "Glavani Park enquiry",
    "---",
    `Name: ${guestName}`,
    `Email: ${guestEmail}`,
    `Phone: ${field(formData, "phone")}`,
    `Activity: ${field(formData, "activity") || "General enquiry"}`,
    `Date: ${field(formData, "date") || "—"}`,
    `Adults: ${field(formData, "adults") || "—"}`,
    `Children: ${field(formData, "children") || "—"}`,
    `Message: ${field(formData, "message")}`,
    "---",
    "Glavani Park · Glavani 10, Barban, Istria",
  ].join("\n");
}

function bookingSubject(guestName: string, guestEmail: string, visitDate: string): string {
  const who = guestName || "Guest";
  const emailPart = guestEmail ? ` (${guestEmail})` : "";
  return `Booking – ${who}${emailPart} – ${visitDate}`;
}

function contactSubject(
  guestName: string,
  guestEmail: string,
  activity: string,
): string {
  const who = guestName || activity;
  const emailPart = guestEmail ? ` (${guestEmail})` : "";
  return `Enquiry – ${who}${emailPart}`;
}

function resolveFromEmail(
  env: Env,
  kind: "booking" | "contact",
): string {
  const legacy = env.RESEND_FROM_EMAIL?.trim();
  if (kind === "booking") {
    return (
      env.RESEND_BOOKING_FROM_EMAIL?.trim() ||
      legacy ||
      DEFAULT_BOOKING_FROM_EMAIL
    );
  }
  return (
    env.RESEND_CONTACT_FROM_EMAIL?.trim() ||
    legacy ||
    DEFAULT_CONTACT_FROM_EMAIL
  );
}

async function sendParkEmail(
  env: Env,
  options: {
    body: string;
    subject: string;
    guestEmail: string;
    guestName: string;
    fromLabel: string;
    fromEmail: string;
  },
): Promise<{ ok: boolean; errors?: string[] }> {
  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return { ok: false, errors: ["RESEND_API_KEY is not configured"] };
  }

  const toEmail = env.RESEND_TO_EMAIL?.trim() || DEFAULT_TO_EMAIL;

  const payload: Record<string, unknown> = {
    from: `${options.fromLabel} <${options.fromEmail}>`,
    to: [toEmail],
    subject: options.subject,
    text: options.body,
  };
  if (options.guestEmail) {
    payload.reply_to = options.guestName
      ? `${options.guestName} <${options.guestEmail}>`
      : options.guestEmail;
  }

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (response.ok) return { ok: true };

  try {
    const data = (await response.json()) as { message?: string };
    return { ok: false, errors: [data.message || response.statusText] };
  } catch {
    return { ok: false, errors: [response.statusText] };
  }
}

export const onRequest: PagesFunction<Env> = (context) => {
  const handler = staticFormsPlugin({
    respondWith: async ({ formData, name }) => {
      if (name === BOOKING_FORM) {
        const guestName = field(formData, "name");
        const guestEmail = field(formData, "email");
        const visitDate = formatBookingDate(
          field(formData, "date"),
          field(formData, "lang"),
        );
        const body = buildBookingEmailBody(formData, guestName, guestEmail);
        const subject = bookingSubject(guestName, guestEmail, visitDate);

        const result = await sendParkEmail(context.env, {
          body,
          subject,
          guestEmail,
          guestName,
          fromLabel: "Glavani Park Booking",
          fromEmail: resolveFromEmail(context.env, "booking"),
        });

        if (!result.ok) {
          return Response.json(
            { ok: false, error: "send_failed", errors: result.errors },
            { status: 500 },
          );
        }
        return Response.json({ ok: true });
      }

      if (name === CONTACT_FORM) {
        if (field(formData, "botcheck")) {
          return Response.json({ ok: true });
        }

        if (contactFormContainsLink(formData)) {
          return Response.json(
            { ok: false, error: "links_not_allowed" },
            { status: 400 },
          );
        }

        const guestName = field(formData, "name");
        const guestEmail = field(formData, "email");
        const activity = field(formData, "activity") || "General enquiry";
        const body = buildContactEmailBody(formData, guestName, guestEmail);
        const subject = contactSubject(guestName, guestEmail, activity);

        const result = await sendParkEmail(context.env, {
          body,
          subject,
          guestEmail,
          guestName,
          fromLabel: "Glavani Park Enquiry",
          fromEmail: resolveFromEmail(context.env, "contact"),
        });

        if (!result.ok) {
          return Response.json(
            { ok: false, error: "send_failed", errors: result.errors },
            { status: 500 },
          );
        }
        return Response.json({ ok: true });
      }

      return Response.json({ ok: false, error: "unknown_form" }, { status: 404 });
    },
  });

  return handler(context);
};
