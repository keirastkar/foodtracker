from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
     

# class Profile(LoginRequiredMixin,generic.CreateView):
#     model = CustomUser
#     form_class=Profile
#     template_name = 'userinfo.html'
#     success_url = reverse_lazy('userinfo')