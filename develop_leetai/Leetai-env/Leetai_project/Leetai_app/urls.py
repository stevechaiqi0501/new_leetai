from django.urls import path
from . import views

app_name = 'Leetai'
urlpatterns = [
    path('',views.HomepageView.as_view(),name='Homepage'),
]