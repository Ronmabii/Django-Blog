from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'), 	
	path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #path('blog/', PostListView.as_view(), name='blog-home') // This is probably extra but keeping as record
]

#path('', PostListView.as_view(), name='blog-home') 	the originals
#path('about/', views.about, name='blog-about')

#path('', views.front_page, name='blog-about'), #// Front 
#path('blog/', PostListView.as_view(), name='blog-posts'), # The good looking but not working