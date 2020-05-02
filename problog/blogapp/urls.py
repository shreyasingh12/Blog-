
from django.urls import path
from .import views
urlpatterns = [
    path("", views.blog_list, name='display')
    path('^(?P<slug>[\w-]+)/$', views.blog_detail, name="detail"),
]
