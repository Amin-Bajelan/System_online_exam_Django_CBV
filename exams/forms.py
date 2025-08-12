from django import forms
from .models import Exam, Question, MultipleChoiceQuestion, DescriptiveQuestion, StudentAnswer
from django.core.exceptions import ValidationError
from datetime import timedelta
from accounts.models import Profile


class ExamForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Exam
        fields = ['title', 'start_time', 'end_time', 'description']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')

        if start and end:
            if start >= end:
                raise ValidationError('End time must be later than the start time.')

            duration = end - start
            if duration.total_seconds() < 15 * 60:  # 15 minutes in seconds
                raise ValidationError('The exam duration must be at least 15 minutes.')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_type']


class MCQForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['image', 'question_diss', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'score']


class DescriptiveForm(forms.ModelForm):
    class Meta:
        model = DescriptiveQuestion
        fields = ['image', 'question_diss', 'question_answer', 'score']


class AssignStudentsForm(forms.ModelForm):
    list_students = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['list_students'].queryset = Profile.objects.filter(username__is_teacher=False)

    class Meta:
        model = Exam
        fields = ['list_students']


class AnswerMultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['mc_answer']


class AnswerDescriptiveForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['desc_answer']


