from django.urls import path,include
from . import views

app_name = 'Leetai'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('inquiry',views.InquiryView.as_view(),name="inquiry"),
    path('question',views.QuestionlistView.as_view(),name="question"),
    path('question/<int:pk>',views.QuestionDetailView.as_view(),name="question_detail"),
    path('question_create',views.QuestionCreateView.as_view(),name='question_create'),
    path('Answerdetail/<int:pk>',views.AnswerDetailview.as_view(),name='answer_detail')
]