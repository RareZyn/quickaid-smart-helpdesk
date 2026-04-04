import uuid

from django.db import models

from tickets.models import Ticket


class EmailLog(models.Model):

    class EmailType(models.TextChoices):
        CONFIRMATION = 'confirmation', 'Confirmation'
        STATUS_UPDATE = 'status_update', 'Status Update'
        ASSIGNMENT = 'assignment', 'Assignment'

    class DeliveryStatus(models.TextChoices):
        SENT = 'sent', 'Sent'
        DELIVERED = 'delivered', 'Delivered'
        FAILED = 'failed', 'Failed'
        BOUNCED = 'bounced', 'Bounced'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='email_logs',
    )
    recipient_email = models.EmailField()
    email_type = models.CharField(max_length=15, choices=EmailType.choices)
    sendgrid_message_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=DeliveryStatus.choices, default=DeliveryStatus.SENT
    )
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'email_logs'
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.email_type} to {self.recipient_email} ({self.status})"
