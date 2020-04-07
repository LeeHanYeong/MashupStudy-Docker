from django.http import Http404
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from utils.drf.viewsets import ModelViewSet, UpdateModelViewSet
from .filters import NoticeFilter
from .models import Notice, Attendance
from .permissions import NoticeAuthorOnlyUpdate, AttendanceUserOrReadOnly
from .serializers import NoticeSerializer, NoticeCreateUpdateSerializer, AttendanceUpdateSerializer


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.with_count()
    filterset_class = NoticeFilter
    permission_classes = (
        permissions.IsAuthenticated,
        NoticeAuthorOnlyUpdate,
    )
    serializer_classes = {
        'list': NoticeSerializer,
        'retrieve': NoticeSerializer,
        'create': NoticeCreateUpdateSerializer,
        'update': NoticeCreateUpdateSerializer,
    }

    def get_queryset(self):
        return self.queryset.with_voted(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AttendanceViewSet(UpdateModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceUpdateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        AttendanceUserOrReadOnly,
    )

    def get_object(self):
        try:
            attendance = super().get_object()
        except (Attendance.DoesNotExist, AssertionError, Http404):
            notice_id = self.request.data.get('notice_id')
            notice = get_object_or_404(Notice, id=notice_id)
            attendance = notice.attendance_set.get(user=self.request.user)
        return attendance
