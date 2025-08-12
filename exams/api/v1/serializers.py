from rest_framework import serializers
from accounts.models import User, Profile
from exams.models import Exam, StudentScore, Question, MultipleChoiceQuestion, DescriptiveQuestion


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'is_active', 'is_teacher']

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class StudentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentScore
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'


class DescriptiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveQuestion
        fields = '__all__'



