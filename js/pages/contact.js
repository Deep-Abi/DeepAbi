/**
 * Contact page.
 *
 * There is no server behind this form, so it does not pretend there is.
 * Submitting validates the fields and then hands the enquiry to the visitor's
 * own email client as a pre-filled message addressed to DeepAbi. Nothing is
 * transmitted by this page, and the confirmation says exactly that.
 *
 * If a real backend is added later, replace the buildMailto()/submit handler
 * with the POST and update the confirmation text to match what actually
 * happens. Do not restore a success message that is not backed by a delivery.
 */
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const toast = document.getElementById('toast');
  if (!form) return;

  const TO = 'hello@deepabi.com';

  function value(id) {
    const el = document.getElementById(id);
    return el ? el.value.trim() : '';
  }

  function buildMailto() {
    const name = value('cf-name');
    const email = value('cf-email');
    const phone = value('cf-phone');
    const service = value('cf-service');
    const message = value('cf-message');

    const subject = service ? `Enquiry: ${service}` : 'Website enquiry';
    const body = [
      `Name: ${name}`,
      `Email: ${email}`,
      phone ? `Phone: ${phone}` : null,
      `Service required: ${service || '(not specified)'}`,
      '',
      message
    ].filter(l => l !== null).join('\n');

    return `mailto:${TO}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    // Hand off to the visitor's mail client. The form is deliberately not
    // reset: if the handoff does not work, their text is still on screen.
    window.location.href = buildMailto();

    if (toast) {
      const msgEl = document.getElementById('toastMsg');
      if (msgEl) {
        msgEl.textContent = 'Your email app should now open with this enquiry ready to send. '
          + 'If nothing opened, email ' + TO + ' directly.';
      }
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 7000);
    }
  });
});
