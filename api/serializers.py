from rest_framework import serializers
from api.models import Questions, Answers

class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Questions
        depth = 2
        fields='__all__'

class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answers
        depth = 2
        fields='__all__'