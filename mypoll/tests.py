from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_create_question(self):
        question = Question.objects.create(question_text ="thai food" pub_date = timezone)
         