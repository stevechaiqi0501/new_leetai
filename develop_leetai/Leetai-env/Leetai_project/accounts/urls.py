from django.urls import path,include
from . import views
from .views import ProfileListView,ProfileupdateView

app_name = 'accounts'

urlpatterns = [
    path('profile',views.ProfileListView.as_view(),name='profile'),
    path('profile/edit/<int:pk>',views.ProfileupdateView.as_view(),name='edit'),
]