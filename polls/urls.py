from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^results/(?P<pk>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^choice/$', views.ChoiceList.as_view(), name='choice'),
    url(r'^question/$', views.QuestionList.as_view(), name='question'),
    url(r'^question_choice/$', views.QuestionChoiceList.as_view(), name='question_choice'),

    url(r'^modify_question/(?P<pk>[0-9]+)/$', views.ModifyQuestion.as_view(), name='modify_question'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
