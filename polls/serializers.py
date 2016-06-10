from rest_framework import serializers
from .models import Question, Choice
from django.contrib.auth.models import User

class user_serializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'question', )

class question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text',)

class choice_serializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text',)

class qns_choice_serializer(serializers.ModelSerializer):
    choice_set = choice_serializer(many=True)   #, read_only=True

    class Meta:
        model = Question
        fields = ('owner', 'question_text', 'choice_set',)

    def create(self, validated_data):
        choice_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        for o_choice in choice_data:
            Choice.objects.create(question=question, **o_choice)
        return question

class mod_qns_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date',)

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance
