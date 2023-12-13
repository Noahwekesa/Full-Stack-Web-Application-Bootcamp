from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'users/signup.html' #or appname/model_view.html
    success_url = 'home'
    form_class = UserRegisterForm
    success_url = "Your Profile Was Created Successfully"
