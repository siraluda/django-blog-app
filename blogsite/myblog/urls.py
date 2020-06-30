from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('signup/', views.signupPage, name='signup'),
    path('post-form/', views.CreatePostView.as_view(),name='create-post'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post-view'),
    path('post/author/<str:username>/', views.AuthorPostsView.as_view(), name='author-posts-view'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(), name='update-post-view'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='delete-post-view'),
] 