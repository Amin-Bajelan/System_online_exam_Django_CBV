from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, View, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import ExamForm, MCQForm, DescriptiveForm, AssignStudentsForm, AnswerMultipleChoiceForm, \
    AnswerDescriptiveForm
from .models import Exam, Question, MultipleChoiceQuestion, DescriptiveQuestion, StudentAnswer, StudentScore
from accounts.models import User, Profile
from django.db.models import Q
from django.utils import timezone


# Create your views here.


class IndexView(TemplateView, LoginRequiredMixin):
    """
    view index page for after login
    """
    template_name = 'exams/index.html'


class CreateExamView(CreateView,LoginRequiredMixin):
    """
    View to create exam for student; belongs to professor
    """
    template_name = 'exams/create_exam.html'
    form_class = ExamForm

    def form_valid(self, form):
        exam = form.save(commit=False)
        exam.owner = self.request.user
        exam.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('add_questions_page', args=[self.object.id])


class AddQuestionsView(TemplateView,LoginRequiredMixin):
    """
    view to crate new exam and question
    """
    template_name = 'exams/add_questions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam = get_object_or_404(Exam, id=self.kwargs['exam_id'])
        context['exam'] = exam
        context['mcq_form'] = MCQForm()
        context['desc_form'] = DescriptiveForm()
        return context

    def post(self, request, *args, **kwargs):
        exam = get_object_or_404(Exam, id=kwargs['exam_id'])

        if 'add_mcq' in request.POST:
            mcq_form = MCQForm(request.POST, request.FILES)
            if mcq_form.is_valid():
                question = Question.objects.create(
                    exam=exam,
                    question_type='multiple_choice'
                )

                mcq_details = mcq_form.save(commit=False)
                mcq_details.question = question
                mcq_details.save()

        elif 'add_desc' in request.POST:
            desc_form = DescriptiveForm(request.POST, request.FILES)
            if desc_form.is_valid():
                question = Question.objects.create(
                    exam=exam,
                    question_type='descriptive'
                )
                desc_details = desc_form.save(commit=False)
                desc_details.question = question
                desc_details.save()

        return redirect(request.path_info)


class AssignStudentsView(UpdateView,LoginRequiredMixin):
    """
    view for assign students to exam
    """
    model = Exam
    form_class = AssignStudentsForm
    template_name = 'exams/assign_students.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        query = self.request.GET.get('q')

        if query:
            form.fields['list_students'].queryset = Profile.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query),
                username__is_teacher=False
            )
        else:
            form.fields['list_students'].queryset = Profile.objects.filter(
                username__is_teacher=False
            )

        return form

    def form_valid(self, form):
        obj_exam = get_object_or_404(Exam, id=self.kwargs['pk'])
        selected_students = form.cleaned_data['list_students']
        obj_exam.list_students.set(selected_students)
        obj_exam.save()
        return super().form_valid(form)


class ShowExamsView(View, LoginRequiredMixin):
    """
    view for show exams for professor
    """
    def post(self, request, *args, **kwargs):
        professor = User.objects.get(id=self.kwargs['pk'])
        exams = Exam.objects.filter(owner=professor)
        return render(request, 'exams/show_exams.html', {'exams': exams})

    def get(self, request, pk):
        professor = User.objects.get(id=self.kwargs['pk'])
        exams = Exam.objects.filter(owner=professor)
        return render(request, 'exams/show_exams.html', {'exams': exams})


class EditExamQuestionView(View, LoginRequiredMixin):
    """
    view for edit exam question
    """
    def post(self, request, pk):
        obj_exam = get_object_or_404(Exam, pk=pk)
        questions = Question.objects.filter(exam=obj_exam)
        question_m = MultipleChoiceQuestion.objects.filter(question__in=questions)
        question_d = DescriptiveQuestion.objects.filter(question__in=questions)
        return render(request, 'exams/edit_exam_question.html', {
            'question_m': question_m,
            'question_d': question_d
        })


class EditMultipleExamView(UpdateView, LoginRequiredMixin):
    """
    view for edit multiple question
    """
    model = MultipleChoiceQuestion
    template_name = 'exams/edit_multiple_exam.html'
    form_class = MCQForm

    def get_success_url(self):
        return reverse('show_exam', args=[self.request.user.id])

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditDescriptionQuestionView(UpdateView, LoginRequiredMixin):
    """
    view for edit description question
    """
    model = DescriptiveQuestion
    template_name = 'exams/edit_desc_question.html'
    form_class = DescriptiveForm

    def get_success_url(self):
        return reverse('show_exam', args=[self.request.user.id])

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ListAvailableExamsView(View, LoginRequiredMixin):
    """
    view for student to see list available exams
    """
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['pk'])
        profile = Profile.objects.get(username=user)
        available_exams = Exam.objects.filter(list_students=profile)
        current_time = timezone.now()
        return render(request, 'exams/list_available_exams.html',
                      context={'exams': available_exams, 'current_time': current_time}
                      )


class AnswerQuestionView(TemplateView, LoginRequiredMixin):
    """
    view for student to answer available question
    """
    template_name = 'exams/answer_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        questions = exam.questions.all()
        context['exam'] = exam
        context['questions'] = questions
        context['answer_mu'] = AnswerMultipleChoiceForm()
        context['answer_des'] = AnswerDescriptiveForm()
        return context

    def post(self, request, *args, **kwargs):
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        question_id = request.POST.get('question_id')
        question = get_object_or_404(Question, id=question_id)

        if question.question_type == 'multiple_choice':
            form = AnswerMultipleChoiceForm(request.POST)
        else:
            form = AnswerDescriptiveForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.student = request.user.profile
            answer.question = question
            answer.exam = exam
            answer.save()
            return redirect(self.get_success_url())
        else:
            context = self.get_context_data(**kwargs)
            if question.question_type == 'multiple_choice':
                context['answer_mu'] = form
            else:
                context['answer_des'] = form
            return self.render_to_response(context)

    def get_success_url(self):
        return self.request.path


class TookExamView(TemplateView, LoginRequiredMixin):
    template_name = 'exams/student_took_exam.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        questions = Question.objects.filter(exam=exam)
        unique_students = Profile.objects.filter(answers__exam=exam).distinct()
        context['exam'] = exam
        context['questions'] = questions
        context['student_answer'] = unique_students

        return self.render_to_response(context)


class StudentAnswerView(TemplateView, LoginRequiredMixin):
    """
    view to see student answer question
    """
    template_name = 'exams/student_answers.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        exam = get_object_or_404(Exam, pk=self.kwargs['pk_exam'])
        profile = Profile.objects.get(username=self.kwargs['stu_pk'])
        student_answer = StudentAnswer.objects.filter(student=profile)
        context['student_answer'] = student_answer
        context['exam'] = exam
        context['profile'] = profile
        return self.render_to_response(context)


class SetScoreView(View, LoginRequiredMixin):
    """
    view to set student score
    """
    def post(self, request, *args, **kwargs):
        score = request.POST.get('score')
        try:
            score = int(score)
        except (TypeError, ValueError):
            return redirect('error_page')
        exam = get_object_or_404(Exam, pk=kwargs['pk_exam'])
        professor_profile = Profile.objects.get(username=exam.owner)
        profile = get_object_or_404(Profile, pk=kwargs['pk_profile'])
        StudentScore.objects.create(
            student=profile,
            professor=professor_profile,
            exam=exam,
            score=score
        )

        return redirect('took_exam', pk=exam.id)


class MyScoreView(TemplateView, LoginRequiredMixin):
    """
    view for student to see scores
    """
    template_name = 'exams/my_score.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['stu_id'])
        profile = Profile.objects.get(username=user)
        student_answer = StudentScore.objects.filter(student=profile)
        context['student_answer'] = student_answer
        return self.render_to_response(context)


class EditScoreView(TemplateView, LoginRequiredMixin):
    """
    view for professor to edit score
    """
    template_name = 'exams/edit_score.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        profile = Profile.objects.get(username=user)
        student_score = StudentScore.objects.filter(professor=profile)
        context['student_score'] = student_score
        return self.render_to_response(context)


class StudentScoreEditView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        score = request.POST.get('score')
        exam = get_object_or_404(Exam, pk=kwargs['exam_id'])
        profile = get_object_or_404(Profile, pk=kwargs['stu_id'])
        professor = request.user.profile

        student_score = get_object_or_404(StudentScore, exam=exam, student=profile)
        student_score.score = score
        student_score.professor = professor
        student_score.save()

        return redirect('edit_score', pk=request.user.pk)
