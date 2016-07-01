from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone
from django.http import HttpResponse

from .serializers import *

from rest_framework import generics

from django.db import IntegrityError, transaction
from datetime import datetime

from django.contrib.auth.models import User

@transaction.atomic
def MultipleDBTransaction(request):

    # return HttpResponse("testing")

    try:
        # newQns = Question.objects.create(question_text='new question', pub_date=datetime.now(), owner=User.objects.all()[0])
        # Choice.objects.create(question=newQns, choice_text='choice 1', votes=0)
        newQns = Question.objects.get(id=29)
        newQns.delete()

    except (IntegrityError, KeyError, Question.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponse("Error: ???")
    else:
        return HttpResponse("Success: ???")

class MultipleObjectList(generics.ListAPIView):
    questions = Question.objects.all()
    choices = Choice.objects.all()

    serializer_class = MultipleObjectSerializer

class ModifyQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = ModifyQuestionSerializer

class QuestionChoiceList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QnsChoiceSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')#[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('choice_text')

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
