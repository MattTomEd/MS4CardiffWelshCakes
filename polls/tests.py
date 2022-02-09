from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Question, Choice


class PollTests(TestCase):

    def setUp(self):
        """ Create a test poll """
        self.poll = Question.objects.create(
            question_text = "Test question",
            pub_date = "2022-01-01"
        )
        self.choice = Choice.objects.create(
            question = Question.objects.get(id=1),
            choice_text = "Test choice",
            votes = "5",
        )

    def test_poll(self):
        """ Test poll content returns correctly """
        poll = Question.objects.get(id=1)
        choice = Choice.objects.get(id=1)
        expected_object_question = f'{poll.question_text}'
        expected_object_choice = f'{choice.choice_text}'
        expected_object_votes = f'{choice.votes}'
        self.assertEquals(expected_object_question, 'Test question')
        self.assertEquals(expected_object_choice, 'Test choice')
        self.assertEquals(expected_object_votes, '5')

    