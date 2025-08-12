from django.urls import path, include
from . import views

urlpatterns = [
    # main page
    path('', views.IndexView.as_view(), name='index'),
    # url for create new exam from professor
    path('create/', views.CreateExamView.as_view(), name='create_exam'),
    # add question to exam, multichoice or description
    path('exam/<int:exam_id>/add_questions/', views.AddQuestionsView.as_view(), name='add_questions_page'),
    # url for assign student to exam(belong to professor)
    path('assign/student/<int:pk>/', views.AssignStudentsView.as_view(), name='assign_student'),
    # url show list of exam (belong to professor)
    path('show/list/<int:pk>/', views.ShowExamsView.as_view(), name='show_exam'),
    # url for see all question for specific exam (belong to professor)
    path("edit/question/<int:pk>/", views.EditExamQuestionView.as_view(), name='edit_exam_question'),
    # url edit multiple choice Question
    path('edit/multiple/question/<int:pk>/', views.EditMultipleExamView.as_view(), name='edit_multiple_exam_question'),
    # url edit descriptive question
    path('edit/description/<int:pk>/', views.EditDescriptionQuestionView.as_view(), name='edit_description_question'),
    # url to see list of available exam (belong to students)
    path('list/my/exams/<int:pk>/', views.ListAvailableExamsView.as_view(), name='list_available_exams'),
    # url for student to set answer of question
    path('answer/exam/<int:pk>/', views.AnswerQuestionView.as_view(), name='answer_exam'),
    # url see list students who took the exam
    path('took/exam/<int:pk>/', views.TookExamView.as_view(), name='took_exam'),
    # url to see student answers
    path('<int:pk_exam>/student/<int:stu_pk>/', views.StudentAnswerView.as_view(), name='student_answer'),
    # url for set score for student
    path('<int:pk_exam>/score/<int:pk_profile>/', views.SetScoreView.as_view(), name='set_score'),
    # url for see list of score(for student)
    path('my/score/<int:stu_id>/', views.MyScoreView.as_view(), name='my_score'),
    # url for edite student score(for professor)
    path('edit/score/<int:pk>/', views.EditScoreView.as_view(), name='edit_score'),
    # url add new score for student(edit score after submit)
    path('<int:exam_id>/score/student/<int:stu_id>/', views.StudentScoreEditView.as_view(), name='add_new_score'),
    # our api urls
    path('api/v1/', include('exams.api.v1.urls')),
]