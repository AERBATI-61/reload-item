from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ActivityView.as_view(), name="activity"),
    path('post-json-view/<int:num_posts>/', PostJsonListView.as_view(), name="post-json-view")
]

