import staticFormsPlugin from "@cloudflare/pages-plugin-static-forms";

const BOOKING_FORM = "glavani-booking";

interface Env {
  RESEND_API_KEY?: string;
}

function field(formData: FormData, key: string): string {
  const value = formData.get(key);
  return value == null ? "" : String(value).trim();
}

function buildEmailBody(formData: FormData): string {
  const message = field(formData, "message");
  if (message) return message;

  const lines = [
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
  ];
  return lines.join("\n");
}

async function sendBookingEmail(
  env: Env,
  body: string,
  subject: string,
  guestEmail: string,
  guestName: string,
): Promise<{ ok: boolean; errors?: string[] }> {
  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return { ok: false, errors: ["RESEND_API_KEY is not configured"] };
  }

  const payload: Record<string, unknown> = {
    from: "Glavani Park Booking <booking@glavanipark.com>",
    to: ["info@glavanipark.com"],
    cc: ["office@glavanipark.com"],
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
      if (name !== BOOKING_FORM) {
        return Response.json({ ok: false, error: "unknown_form" }, { status: 404 });
      }

      const guestName = field(formData, "name");
      const guestEmail = field(formData, "email");
      const visitDate = field(formData, "date") || "date TBC";
      const body = buildEmailBody(formData);
      const subject = `Glavani Park booking request – ${visitDate}`;

      const result = await sendBookingEmail(
        context.env,
        body,
        subject,
        guestEmail,
        guestName,
      );

      if (!result.ok) {
        return Response.json(
          { ok: false, error: "send_failed", errors: result.errors },
          { status: 500 },
        );
      }

      return Response.json({ ok: true });
    },
  });

  return handler(context);
};
