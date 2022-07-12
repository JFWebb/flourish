from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('posts/', views.posts_index, name='posts'),
    path('posts/<int:post_id>', views.posts_detail, name='detail'),
    path('posts/create', views.add_post, name='post_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]