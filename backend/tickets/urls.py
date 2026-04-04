from django.urls import path

from . import views

urlpatterns = [
    path('tickets', views.TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<str:ticket_id>', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/<str:ticket_id>/status', views.TicketStatusUpdateView.as_view(), name='ticket-status-update'),
    path('tickets/<str:ticket_id>/assign', views.TicketAssignView.as_view(), name='ticket-assign'),
    path('tickets/<str:ticket_id>/notes', views.TicketNoteCreateView.as_view(), name='ticket-note-create'),
    path('admin/tickets', views.AdminTicketListView.as_view(), name='admin-ticket-list'),
]
