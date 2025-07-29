from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User


class Exam(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = (
        ('multiple_choice', 'Multiple Choice'),
        ('descriptive', 'Descriptive'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    text = models.TextField()
    score = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.text[:50]}..."


class MultipleChoiceQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='mc_details')
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f"MCQ for: {self.question.text[:30]}"


class DescriptiveQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='desc_details')
    question_diss = models.TextField(blank=True, null=True)
    question_answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Descriptive for: {self.question.text[:30]}"


