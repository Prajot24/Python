from django.urls import path
from home.views import *

urlpatterns = [
    path('',home),
    path('post-todo',post_todo),
    path('get-todo',get_todo),
]
