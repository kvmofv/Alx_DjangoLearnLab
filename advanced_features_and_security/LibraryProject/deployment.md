#  Deployment HTTPS Configuration

- Use a trusted SSL/TLS certificate (e.g., Let’s Encrypt or commercial).
- Configure your web server (Nginx, Apache) with:
  - SSL certificate & private key paths.
  - Redirect all HTTP traffic to HTTPS.
  - Add HSTS headers in server config (can be redundant if Django already does it).
- Example Nginx snippet:

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    ...
}
