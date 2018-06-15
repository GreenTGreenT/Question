from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)

class Vote(models.Model):
    connect = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)
    vote_true = models.IntegerField(default=0)
    vote_false = models.IntegerField(default=0)

