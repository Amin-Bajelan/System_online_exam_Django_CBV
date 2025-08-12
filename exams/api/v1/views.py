from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, ExamSerializer, StudentScoreSerializer, QuestionSerializer, \
    MultipleChoiceQuestionSerializer, DescriptiveQuestionSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from accounts.models import User

from exams.models import Exam, StudentScore, Question, MultipleChoiceQuestion, DescriptiveQuestion


class CreateUser(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateExamApi(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class DetailExamApi(RetrieveUpdateDestroyAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CreateStudentScoreApi(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = StudentScore.objects.all()
    serializer_class = StudentScoreSerializer


class CreateQuestionApi(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CreateMultipleChoiceQuestionApi(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer


class MultipleChoiceQuestionApi(RetrieveUpdateDestroyAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer


class CreateDescriptiveQuestionApi(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = DescriptiveQuestion.objects.all()
    serializer_class = DescriptiveQuestionSerializer


class DescriptiveQuestionApi(RetrieveUpdateDestroyAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    queryset = DescriptiveQuestion.objects.all()
    serializer_class = DescriptiveQuestionSerializer
