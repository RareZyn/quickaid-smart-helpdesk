from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    AdminNoteCreateSerializer,
    AdminNoteSerializer,
    TicketAssignSerializer,
    TicketCreateSerializer,
    TicketDetailSerializer,
    TicketListSerializer,
    TicketStatusUpdateSerializer,
)
from .services import (
    add_admin_note,
    assign_ticket,
    create_ticket,
    get_all_tickets,
    get_ticket_by_id,
    get_tickets_by_email,
    update_ticket_status,
)


class TicketListCreateView(APIView):
    """
    POST /api/tickets       — create ticket (no auth)
    GET  /api/tickets?email= — get tickets by email (no auth)
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = create_ticket(serializer.validated_data)
        return Response(
            TicketDetailSerializer(ticket).data, status=status.HTTP_201_CREATED
        )

    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response(
                {'error': 'email query parameter is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        tickets = get_tickets_by_email(email)
        return Response(TicketListSerializer(tickets, many=True).data)


class TicketDetailView(APIView):
    """GET /api/tickets/{ticketId}"""
    permission_classes = [AllowAny]

    def get(self, request, ticket_id):
        ticket = get_ticket_by_id(ticket_id)
        if not ticket:
            return Response(
                {'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(TicketDetailSerializer(ticket).data)


class TicketStatusUpdateView(APIView):
    """PUT /api/tickets/{ticketId}/status"""
    permission_classes = [IsAuthenticated]

    def put(self, request, ticket_id):
        serializer = TicketStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = update_ticket_status(
            ticket_id, serializer.validated_data, request.user
        )
        return Response(TicketDetailSerializer(ticket).data)


class TicketAssignView(APIView):
    """PUT /api/tickets/{ticketId}/assign (admin only)"""
    permission_classes = [IsAuthenticated]

    def put(self, request, ticket_id):
        serializer = TicketAssignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = assign_ticket(ticket_id, serializer.validated_data, request.user)
        return Response(TicketDetailSerializer(ticket).data)


class AdminTicketListView(APIView):
    """GET /api/admin/tickets — all tickets with filters (admin only)"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = get_all_tickets(request.query_params)
        return Response(TicketListSerializer(tickets, many=True).data)


class TicketNoteCreateView(APIView):
    """POST /api/tickets/{ticketId}/notes"""
    permission_classes = [IsAuthenticated]

    def post(self, request, ticket_id):
        serializer = AdminNoteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = add_admin_note(ticket_id, serializer.validated_data, request.user)
        return Response(
            AdminNoteSerializer(note).data, status=status.HTTP_201_CREATED
        )
