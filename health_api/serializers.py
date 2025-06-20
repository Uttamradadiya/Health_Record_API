from rest_framework import serializers
from .models import HealthRecord, Comment

# The `HealthRecordSerializer` includes nested comments (read-only). This prevents users from faking comments or assigning themselves.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('doctor',)

class HealthRecordSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = HealthRecord
        fields = '__all__'
        read_only_fields = ('patient',)
