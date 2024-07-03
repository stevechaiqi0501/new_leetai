from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
class HomepageView(generic.TemplateView):
    template_name = 'Homepage.html'
    
class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
