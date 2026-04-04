from rest_framework import serializers

from users.serializers import UserMinimalSerializer

from .models import AdminNote, StatusHistory, Ticket


class StatusHistorySerializer(serializers.ModelSerializer):
    changed_by = UserMinimalSerializer(read_only=True)

    class Meta:
        model = StatusHistory
        fields = ['id', 'previous_status', 'new_status', 'changed_by', 'notes', 'changed_at']


class AdminNoteSerializer(serializers.ModelSerializer):
    author = UserMinimalSerializer(read_only=True)

    class Meta:
        model = AdminNote
        fields = ['id', 'author', 'content', 'created_at']


class AdminNoteCreateSerializer(serializers.Serializer):
    content = serializers.CharField()


class TicketCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    display_name = serializers.CharField(max_length=255)
    subject = serializers.CharField(max_length=255)
    description = serializers.CharField()
    category = serializers.ChoiceField(choices=Ticket.Category.choices)
    priority = serializers.ChoiceField(
        choices=Ticket.Priority.choices, default='Medium'
    )


class TicketListSerializer(serializers.ModelSerializer):
    user = UserMinimalSerializer(read_only=True)
    assigned_to = UserMinimalSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'ticket_id', 'user', 'subject', 'category',
            'priority', 'status', 'assigned_to', 'created_at', 'updated_at',
        ]


class TicketDetailSerializer(serializers.ModelSerializer):
    user = UserMinimalSerializer(read_only=True)
    assigned_to = UserMinimalSerializer(read_only=True)
    status_history = StatusHistorySerializer(many=True, read_only=True)
    admin_notes = AdminNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'ticket_id', 'user', 'subject', 'description', 'category',
            'priority', 'status', 'assigned_to', 'created_at', 'updated_at',
            'resolved_at', 'status_history', 'admin_notes',
        ]


class TicketStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Ticket.Status.choices)
    notes = serializers.CharField(required=False, allow_blank=True)


class TicketAssignSerializer(serializers.Serializer):
    assigned_to = serializers.UUIDField()
