from django.urls import path,include
from . import views
from .views import ProfileListView

app_name = 'accounts'

urlpatterns = [
    path('profile/edit',views.ProfileListView.as_view(),name='profile'),
]