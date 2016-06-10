from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic


from .models import Choice, Question
from django.utils import timezone
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from polls.serializers import * #question_serializer, user_serializer, choice_serializer, qns_choice_serializer,

from rest_framework import status
# from rest_framework.decorators import api_view
#
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from polls.permissions import IsOwnerOrReadOnly


class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

class user_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer


class RUD_qns(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = mod_qns_serializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class qns_choice_list(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = qns_choice_serializer

class create_qns_choice(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = qns_choice_serializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


    # def perform_create(self, serializer):
    #     serializer.save(True)

###get all choices, get all questions###
class choice_list(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = choice_serializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(True)

class question_list(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = question_serializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(True)

###create choices, create questions###
class create_question(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = question_serializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class create_choice(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = choice_serializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')#[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
