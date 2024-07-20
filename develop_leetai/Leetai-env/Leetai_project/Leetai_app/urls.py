from django.urls import path,include
from . import views

app_name = 'Leetai'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('inquiry',views.InquiryView.as_view(),name="inquiry"),
    path('question',views.QuestionlistView.as_view(),name="question"),
    path('question/<int:pk>',views.DetailQuestionView.as_view(),name="question_detail")
]