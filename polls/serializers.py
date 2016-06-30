from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text',)

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text',)

class QnsChoiceSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('owner', 'question_text', 'choice_set',)

    def create(self, validated_data):
        choice_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        for o_choice in choice_data:
            Choice.objects.create(question=question, **o_choice)
        return question

class ModifyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date',)

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance
