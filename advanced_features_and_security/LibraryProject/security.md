## Security Measures

- DEBUG is False to prevent debug info leaks.
- Browser protections: XSS filter, clickjacking denial, MIME sniffing disabled.
- CSRF tokens added to all POST forms.
- Cookies marked secure for HTTPS.
- Content Security Policy set using django-csp middleware.
- Views only use Django ORM and forms — no raw SQL, safe input validation.


# ✅ HTTPS & Secure Headers Review

- `SECURE_SSL_REDIRECT` forces HTTPS for all requests.
- HSTS settings ensure browsers only connect over HTTPS for one year.
- Secure cookies prevent session hijacking over HTTP.
- Headers `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_BROWSER_XSS_FILTER` protect against clickjacking, MIME sniffing, and XSS.
- SSL/TLS must be correctly set on the server to support HTTPS fully.

Potential Improvements:
- Use a Content Security Policy (CSP) with strict rules.
- Rotate certificates regularly.
- Monitor for expired certs.
