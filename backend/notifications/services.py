def send_ticket_confirmation_email(ticket):
    """Send confirmation email to submitter via SendGrid after ticket creation.
    Log result to EmailLog."""
    pass


def send_status_update_email(ticket, previous_status: str, new_status: str):
    """Send status change notification to submitter via SendGrid.
    Log result to EmailLog."""
    pass


def send_assignment_notification_email(ticket, assigned_to_user):
    """Send assignment notification to the support staff member via SendGrid.
    Log result to EmailLog."""
    pass


def log_email(ticket, recipient_email: str, email_type: str,
              sendgrid_message_id: str = None, delivery_status: str = 'sent'):
    """Create an EmailLog record."""
    pass
