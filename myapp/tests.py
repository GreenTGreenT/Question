from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from myapp.models import Question, Vote

        

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        
        frist_question = Question()
        frist_question.question_text = 'Human have 2 eyes'
        frist_question.save()
        frist_answer = Question()
 
        second_question = Question()
        second_question.question_text = 'Human have 3 ears'
        second_question.save()
        second_answer = Question()

        save_item = Question.objects.all() 
        self.assertEqual(save_item.count(),2)

        first_saved_item = save_item[0]
        second_saved_item =save_item[1]
        self.assertEqual(first_saved_item.question_text, 'Human have 2 eyes')
        self.assertEqual(second_saved_item.question_text, 'Human have 3 ears')


    def test_can_vote(self):
        list_question = Question()
        list_question.save()

        frist_vote = Vote()
        frist_vote.vote_true = '1'
        frist_vote.connect = list_question
        frist_vote.save()

        second_vote = Vote()
        second_vote.vote_false = '1'
        second_vote.connect = list_question
        second_vote.save()

        saved_vote = Vote.objects.all()
        self.assertEqual(saved_vote.count(), 2)
       
        first_saved_vote = saved_vote[0]
        second_saved_vote = saved_vote[1]
        self.assertEqual(first_saved_vote.vote_true, 1)
        self.assertEqual(first_saved_vote.connect, list_question)
        self.assertEqual(second_saved_vote.vote_false, 1)
        self.assertEqual(second_saved_vote.connect, list_question)

