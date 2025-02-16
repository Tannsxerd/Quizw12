from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice

class QuestionModelTests(TestCase):
    def test_create_question(self):
        """Test that a Question can be created and has correct attributes."""
        question = Question.objects.create(question_text="What's new?", pub_date=timezone.now())
        self.assertEqual(question.question_text, "What's new?")
        self.assertTrue(isinstance(question.pub_date, timezone.datetime))

    def test_question_str(self):
        """Test the string representation of the Question model."""
        question = Question.objects.create(question_text="Test Question", pub_date=timezone.now())
        self.assertEqual(str(question), "Test Question")

class ChoiceModelTests(TestCase):
    def test_create_choice(self):
        """Test that a Choice can be created and linked to a Question."""
        question = Question.objects.create(question_text="Test Question", pub_date=timezone.now())
        choice = Choice.objects.create(question=question, choice_text="Choice 1", votes=5)
        self.assertEqual(choice.choice_text, "Choice 1")
        self.assertEqual(choice.votes, 5)
        self.assertEqual(choice.question, question)

    def test_choice_str(self):
        """Test the string representation of the Choice model."""
        question = Question.objects.create(question_text="Test Question", pub_date=timezone.now())
        choice = Choice.objects.create(question=question, choice_text="Choice 1", votes=0)
        self.assertEqual(str(choice), "Choice 1")
