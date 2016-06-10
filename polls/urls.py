from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^results/(?P<pk>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
    url(r'^users/$', views.user_list.as_view(), name='user-list'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^qns/$', views.question_list.as_view(), name='qns'),
    url(r'^cho/$', views.choice_list.as_view(), name='cho'),
    url(r'^qnsc/$', views.create_question.as_view(), name='qnsc'),
    url(r'^choc/$', views.create_choice.as_view(), name='choc'),
    url(r'^qns_cho/$', views.qns_choice_list.as_view(), name='qns_cho'),
    url(r'^qnsc_choc/$', views.create_qns_choice.as_view(), name='qnsc_choc'),
    url(r'^mod_qns/(?P<pk>[0-9]+)/$', views.RUD_qns.as_view(), name='mod_qns'),
#    url(r'^users/(?P<pk>[0-9]+)/$', views.question_list.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
