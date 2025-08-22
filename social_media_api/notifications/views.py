from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from . serializers import NotificationSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Notification.objects.filter(recipient=self.request.user).order_by("is_read", "-timestamp")
        unread = self.request.query_params.get("unread")
        if unread == "true":
            qs = qs.filter(is_read=False)
        return qs

    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"status": "marked as read"}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["post"])
    def mark_all_as_read(self, request):
        self.get_queryset().update(is_read=True)
        return Response({"status": "all marked as read"}, status=status.HTTP_200_OK)