/**
 * Contact page JS: client-side validation and success toast for the
 * contact form. No backend is wired up — see README for how to connect
 * this to an email service or serverless function.
 */
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const toast = document.getElementById('toast');
  if (!form || !toast) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    const msgEl = document.getElementById('toastMsg');
    if (msgEl) msgEl.textContent = "Message sent successfully! We'll be in touch within one business day.";
    toast.classList.add('show');
    form.reset();
    setTimeout(() => toast.classList.remove('show'), 4500);
  });
});
