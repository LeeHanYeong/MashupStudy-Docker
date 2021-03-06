from rest_framework import serializers

from utils.drf.serializers import ModelSerializer
from ..models import Attendance


class AttendanceUpdateSerializer(ModelSerializer):
    notice_id = serializers.IntegerField(
        required=False, write_only=True,
        help_text='지정시 /api/attendances/에 바로 요청 가능')

    class Meta:
        model = Attendance
        fields = (
            'notice_id',
            'vote',
        )
