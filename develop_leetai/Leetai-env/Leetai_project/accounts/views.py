from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import CustomUser
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class ProfileListView(generic.ListView):
    template_name='edit_profile.html'
    model = CustomUser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customuser_list']=context['customuser_list'].filter(username=self.request.user)
        return context
    
class ProfileupdateView(UpdateView):
    template_name ='edit.html'
    model = CustomUser
    fields = ['picture','username','email','sex','discription']
    success_url=reverse_lazy("index.html")