# DeliveryHub

**Professional delivery booking & management platform** for customers and courier businesses. Built for Nigeria with international expansion ready.

### Live Demo & Source
- **GitHub Repository**: https://github.com/Emmyreign100/deliveryhub
- One-click deploy on Render: [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Emmyreign100/deliveryhub)

### Features
- Customer registration, booking, online parcel tracking
- Courier business registration and order management
- Admin dashboard for full control and revenue tracking
- Monetization: 10% disclosed commission on completed bookings + subscription stubs (Paystack/Stripe)
- Expanded delivery statuses, interactive maps (Leaflet), email/SMS notification stubs, mobile-friendly UI

### Demo Credentials
- **Admin**: `admin` / `admin123`
- Register your own Customer or Courier accounts

### Quick Start
```bash
git clone https://github.com/Emmyreign100/deliveryhub.git
cd deliveryhub
pip install -r requirements.txt
python app.py
```

### Deployment Notes
- Recommended: Render, Railway, or Fly.io (persistent disk for SQLite or switch to PostgreSQL)
- Vercel requires serverless adaptation (functions)
- For production: Use PostgreSQL, real payment webhooks, and SMS/email providers (Termii, Twilio, SendGrid)

Built with Flask, Bootstrap 5, and Leaflet. Ready for Nigeria and global expansion.
