from django.urls import path, include
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('post/create', views.create_post, name='create_post'),
    #path('',include("users.urls")),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('post_create/', views.create_post, name='post-create'),
    path('post/delete/<int:id>', views.delete_post, name='post-delete'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
]
