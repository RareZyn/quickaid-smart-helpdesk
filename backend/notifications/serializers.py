from rest_framework import serializers

from .models import EmailLog


class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = [
            'id', 'ticket', 'recipient_email', 'email_type',
            'sendgrid_message_id', 'status', 'sent_at',
        ]
