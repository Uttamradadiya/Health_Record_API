from rest_framework import serializers
from .models import HealthRecord, Comment

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
