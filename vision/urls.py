from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('',views.index),
    path('post/<slug:slug>',views.show_post,name='detailview')
]