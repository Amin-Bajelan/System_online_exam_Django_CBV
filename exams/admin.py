from django.contrib import admin
from .models import Exam, Question, MultipleChoiceQuestion, DescriptiveQuestion, StudentAnswer, StudentScore


# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'start_time', 'end_time')
    list_filter = ('owner', 'start_time', 'end_time')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['exam', 'question_type']
    list_filter = ('exam', 'question_type')


class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_filter = ('question',)


class DescriptiveQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_diss']
    list_filter = ('question', 'question_diss')


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'question')
    list_filter = ('student', 'exam', 'question')


class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'professor', 'score', 'exam')
    list_filter = ('student', 'professor', 'score', 'exam')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(DescriptiveQuestion, DescriptiveQuestionAdmin)
admin.site.register(StudentAnswer, StudentAnswerAdmin)
admin.site.register(StudentScore, StudentScoreAdmin)
