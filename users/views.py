from django.views.generic import CreateView
from .forms import RegularUserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = RegularUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
