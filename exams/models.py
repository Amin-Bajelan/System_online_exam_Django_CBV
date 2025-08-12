from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User
from accounts.models import Profile


class Exam(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    list_students = models.ManyToManyField(Profile, blank=True, null=True)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = (
        ('multiple_choice', 'Multiple Choice'),
        ('descriptive', 'Descriptive'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return f"{self.question_type[:50]}..."


class MultipleChoiceQuestion(models.Model):
    image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='mc_details')
    question_diss = models.TextField(blank=False, null=False)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    score = models.FloatField(default=1.0)
    correct_option = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f"MCQ for: {self.question.text[:30]}"


class DescriptiveQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='desc_details')
    image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    question_diss = models.TextField(blank=False, null=False)
    question_answer = models.TextField(blank=True, null=True)
    score = models.FloatField(default=1.0)

    def __str__(self):
        return f"Descriptive for: {self.question.text[:30]}"


class StudentAnswer(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='answers')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    mc_answer = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    desc_answer = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.question}"


class StudentScore(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='score')
    professor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='student_scores')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student_scores')
    score = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.score}"
