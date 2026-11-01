"""Notification stubs for Email and SMS.
In production, integrate with:
- Email: Flask-Mail, SendGrid, AWS SES
- SMS: Twilio, Termii (Nigeria), Africa's Talking
"""

def send_email(to_email, subject, body):
    print(f"[EMAIL STUB] To: {to_email}")
    print(f"[EMAIL STUB] Subject: {subject}")
    print(f"[EMAIL STUB] Body: {body}")
    print("-" * 50)
    return True

def send_sms(to_phone, message):
    print(f"[SMS STUB] To: {to_phone}")
    print(f"[SMS STUB] Message: {message}")
    print("-" * 50)
    return True

def notify_booking_created(delivery, customer):
    subject = f"Delivery Booked - {delivery.tracking_id}"
    body = f"Your delivery has been booked.\nTracking ID: {delivery.tracking_id}\nPickup: {delivery.pickup_address}\nDropoff: {delivery.dropoff_address}\nPrice: {delivery.currency} {delivery.price}"
    send_email(customer.email, subject, body)
    if customer.phone:
        send_sms(customer.phone, f"Delivery booked! Tracking: {delivery.tracking_id}")

def notify_status_update(delivery, customer, courier=None):
    subject = f"Delivery Update - {delivery.tracking_id}: {delivery.status.upper()}"
    body = f"Status updated to: {delivery.status}\nTracking ID: {delivery.tracking_id}"
    send_email(customer.email, subject, body)
    if customer.phone:
        send_sms(customer.phone, f"Delivery {delivery.tracking_id} is now {delivery.status}")
    if courier and courier.phone:
        send_sms(courier.phone, f"Order {delivery.tracking_id} status: {delivery.status}")
