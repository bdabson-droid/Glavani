import staticFormsPlugin from "@cloudflare/pages-plugin-static-forms";

const BOOKING_FORM = "glavani-booking";
const CONTACT_FORM = "glavani-contact";

interface Env {
  RESEND_API_KEY?: string;
  RESEND_FROM_EMAIL?: string;
  RESEND_TO_EMAIL?: string;
}

const DEFAULT_FROM_EMAIL = "info@glavani-park.com";
const DEFAULT_TO_EMAIL = "info@glavanipark.com";

function field(formData: FormData, key: string): string {
  const value = formData.get(key);
  return value == null ? "" : String(value).trim();
}

function buildBookingEmailBody(formData: FormData): string {
  const message = field(formData, "message");
  if (message) return message;

  return [
    field(formData, "header") || "Glavani Park booking request",
    "---",
    `Package: ${field(formData, "package")}`,
    `Date: ${field(formData, "date")}`,
    `Arrival: ${field(formData, "arrival")}`,
    `Guests: ${field(formData, "guests")}`,
    `Adults: ${field(formData, "adults")}`,
    `Children: ${field(formData, "children")}`,
    `Total: ${field(formData, "total")}`,
    `Name: ${field(formData, "name")}`,
    `Email: ${field(formData, "email")}`,
    `Phone: ${field(formData, "phone")}`,
    `Notes: ${field(formData, "notes") || "—"}`,
    "---",
    "Glavani Park · Glavani 10, Barban, Istria",
  ].join("\n");
}

function buildContactEmailBody(formData: FormData): string {
  return [
    "Glavani Park enquiry",
    "---",
    `Name: ${field(formData, "name")}`,
    `Email: ${field(formData, "email")}`,
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

async function sendParkEmail(
  env: Env,
  body: string,
  subject: string,
  guestEmail: string,
  guestName: string,
  fromLabel: string,
): Promise<{ ok: boolean; errors?: string[] }> {
  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return { ok: false, errors: ["RESEND_API_KEY is not configured"] };
  }

  const fromEmail = env.RESEND_FROM_EMAIL?.trim() || DEFAULT_FROM_EMAIL;
  const toEmail = env.RESEND_TO_EMAIL?.trim() || DEFAULT_TO_EMAIL;

  const payload: Record<string, unknown> = {
    from: `${fromLabel} <${fromEmail}>`,
    to: [toEmail],
    subject,
    text: body,
  };
  if (guestEmail) {
    payload.reply_to = guestName ? `${guestName} <${guestEmail}>` : guestEmail;
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
        const visitDate = field(formData, "date") || "date TBC";
        const body = buildBookingEmailBody(formData);
        const subject = `Glavani Park booking request – ${visitDate}`;

        const result = await sendParkEmail(
          context.env,
          body,
          subject,
          guestEmail,
          guestName,
          "Glavani Park Booking",
        );

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

        const guestName = field(formData, "name");
        const guestEmail = field(formData, "email");
        const activity = field(formData, "activity") || "General enquiry";
        const body = buildContactEmailBody(formData);
        const subject = `Glavani Park enquiry – ${guestName || activity}`;

        const result = await sendParkEmail(
          context.env,
          body,
          subject,
          guestEmail,
          guestName,
          "Glavani Park Enquiry",
        );

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
