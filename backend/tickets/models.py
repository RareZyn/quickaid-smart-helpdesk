import uuid

from django.conf import settings
from django.db import models


class Ticket(models.Model):

    class Category(models.TextChoices):
        IT_SUPPORT = 'IT Support', 'IT Support'
        FACILITIES = 'Facilities', 'Facilities'
        ACADEMIC_SERVICES = 'Academic Services', 'Academic Services'
        LIBRARY = 'Library', 'Library'
        FINANCE = 'Finance', 'Finance'
        GENERAL_INQUIRY = 'General Inquiry', 'General Inquiry'

    class Priority(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'
        URGENT = 'Urgent', 'Urgent'

    class Status(models.TextChoices):
        OPEN = 'Open', 'Open'
        IN_PROGRESS = 'In Progress', 'In Progress'
        RESOLVED = 'Resolved', 'Resolved'
        CLOSED = 'Closed', 'Closed'

    ticket_id = models.CharField(max_length=20, primary_key=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitted_tickets',
    )
    subject = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices)
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.MEDIUM
    )
    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.OPEN
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tickets'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = self._generate_ticket_id()
        super().save(*args, **kwargs)

    @staticmethod
    def _generate_ticket_id():
        last_ticket = (
            Ticket.objects.order_by('-created_at')
            .values_list('ticket_id', flat=True)
            .first()
        )
        if last_ticket:
            last_num = int(last_ticket.split('-')[1])
            return f"QA-{last_num + 1:05d}"
        return "QA-00001"

    def __str__(self):
        return f"{self.ticket_id}: {self.subject}"


class StatusHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='status_history',
    )
    previous_status = models.CharField(max_length=15, choices=Ticket.Status.choices)
    new_status = models.CharField(max_length=15, choices=Ticket.Status.choices)
    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    notes = models.TextField(null=True, blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'status_history'
        ordering = ['-changed_at']

    def __str__(self):
        return f"{self.ticket.ticket_id}: {self.previous_status} -> {self.new_status}"


class AdminNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='admin_notes',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admin_notes',
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admin_notes'
        ordering = ['-created_at']

    def __str__(self):
        return f"Note on {self.ticket.ticket_id} by {self.author.display_name}"
