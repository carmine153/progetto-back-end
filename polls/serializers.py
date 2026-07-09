from rest_framework import serializers
from .models import Poll, Choice
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'votes']
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'created_by', 'created_at','choices']
        read_only_fields = ['created_by']
        