from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from forum import views as user_views
from .views import ForumListView, ForumPostsListView, ForumPostDetailView

app_name = 'forum'

urlpatterns = [
    path('', ForumListView.as_view(), name='home'),
    path('<str:pk>/', ForumPostsListView.as_view(), name='forums-list'),
    path('<forum>/<str:str>/<str:pk>/', ForumPostDetailView.as_view(), name='post-detail'),
    #Backwards
    path('<forum>/', ForumPostDetailView.as_view(), name='forum-board'),


]