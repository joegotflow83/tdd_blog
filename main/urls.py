from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^create/post/$', views.CreatePost.as_view(), name='create_post'),
]
