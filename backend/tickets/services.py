def create_ticket(validated_data: dict):
    """Create a new ticket, get-or-create the user by email,
    generate QA-XXXXX ID, trigger confirmation email."""
    pass


def get_tickets_by_email(email: str):
    """Return all tickets submitted by the given email address."""
    pass


def get_ticket_by_id(ticket_id: str):
    """Return a single ticket with prefetched status_history and admin_notes,
    or None if not found."""
    pass


def update_ticket_status(ticket_id: str, validated_data: dict, changed_by):
    """Update ticket status, create StatusHistory record, set resolved_at
    if status is 'Resolved', trigger status update email."""
    pass


def assign_ticket(ticket_id: str, validated_data: dict, assigned_by):
    """Assign ticket to a support staff user (admin only). Change status to
    'In Progress' if currently 'Open'. Trigger assignment notification email."""
    pass


def get_all_tickets(query_params: dict):
    """Return all tickets with optional filters: status, category, priority,
    assigned_to, date range (date_from, date_to)."""
    pass


def add_admin_note(ticket_id: str, validated_data: dict, author):
    """Create an AdminNote attached to the given ticket."""
    pass
