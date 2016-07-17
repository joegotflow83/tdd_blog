from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Post


class Home(TemplateView):
    """Home page when users login"""
    template_name = 'main/home.html'


class CreatePost(CreateView):
    """Users can create posts"""
    model = Post
    fields = ('title', 'body')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')
