from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, default=None)
    choice_text1 = models.CharField(max_length=200, default=None)
    choice_text2 = models.CharField(max_length=200, default=None)
    the_answer = models.CharField(max_length=200, default=None)

class Vote(models.Model):
    connect = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)
    vote_true = models.IntegerField(default=0)
    vote_false = models.IntegerField(default=0)

