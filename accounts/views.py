from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse


class Signup(CreateView):
    """Users can sign up"""
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')
