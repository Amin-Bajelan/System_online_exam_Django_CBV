from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Register a new user
    path('signup/', views.CreateUser.as_view(), name='signup_api'),
    # Obtain JWT token using email and password
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refresh JWT access token using refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Create a new exam (admin only)
    path('create/exam/', views.CreateExamApi.as_view(), name='create_exam_api'),
    # Retrieve details of a specific exam by its ID
    path('detail/exam/<int:pk>/', views.DetailExamApi.as_view(), name='detail_exam'),
    # Submit a student's score (admin or teacher only)
    path('add/score/', views.CreateStudentScoreApi.as_view(), name='set_score_student'),
    # Create a general question
    path('cearete/question/', views.CreateQuestionApi.as_view(), name='create_question'),
    # Add a multiple-choice question to an exam
    path('add/multiplechoise/question/', views.CreateMultipleChoiceQuestionApi.as_view(), name='create_multiple_choice'),
    # Retrieve or update a specific multiple-choice question by its ID
    path('multiplechoise/question/<int:pk>/', views.MultipleChoiceQuestionApi.as_view(), name='multiple_choice'),
    # Add a descriptive (written) question to an exam
    path('add/descriptive/questionn/', views.CreateDescriptiveQuestionApi.as_view(), name='create_descriptive_question'),
    # Retrieve or update a specific descriptive question by its ID
    path('descriptive/question/<int:pk>/', views.DescriptiveQuestionApi.as_view(), name='descriptive_question'),
]