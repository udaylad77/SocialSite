from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.


class SignUp(CreateView):
    """
    Create a 'SignUp' class for SignUp and it's inherit from 'CreateView'.
    """
    form_class = forms.UserCreateForm
    # Once someone has successfully sign up, reverse them back to the login page.
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

