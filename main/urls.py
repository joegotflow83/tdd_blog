from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^post/create/$', views.CreatePost.as_view(), name='create_post'),
    url(r'^post/list/$', views.ListPosts.as_view(), name='list_posts'),
    url(r'^post/(?P<pk>\d+)/$', views.SinglePost.as_view(), name='single_post'),
]
