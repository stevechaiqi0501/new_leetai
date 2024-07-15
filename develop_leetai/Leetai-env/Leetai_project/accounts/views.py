from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import CustomUser
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class ProfileListView(generic.ListView):
    template_name='edit_profile.html'
    model = CustomUser
    success_url=reverse_lazy("index.html")
    
    def get_object(self):
        return self.request.user