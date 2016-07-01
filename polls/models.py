import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='question', default=1)

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        if self.pub_date == None :
            return False
        else:
            return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
