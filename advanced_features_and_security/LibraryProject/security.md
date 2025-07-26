## Security Measures

- DEBUG is False to prevent debug info leaks.
- Browser protections: XSS filter, clickjacking denial, MIME sniffing disabled.
- CSRF tokens added to all POST forms.
- Cookies marked secure for HTTPS.
- Content Security Policy set using django-csp middleware.
- Views only use Django ORM and forms — no raw SQL, safe input validation.
