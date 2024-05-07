from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm, RegisterForm, LoginForm
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms

def home(request):
  posts = Post.objects.all()
  context = {'posts': posts}
  return render(request, 'home.html', context)

#Создание постов  
@login_required  
def create_post(request):
  if request.method == 'GET':
    context = {'form':PostForm()}
    return render(request, 'post_form.html',context)
  elif request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "The post has been created successfully")
      return redirect("home")
    else:
      messages.error(request, 'Please correct the following errors:')
      return render(request, 'post_form.html',{'form':form})

#Удаление постов
@login_required
def delete_post(request, id):
  post = get_object_or_404(Post, pk=id)
  context = {'post':post}
  
  if request.method == 'POST':
      post.delete()
      messages.success(request, 'The post has been deleated')
      return redirect('home')
#Редактирование постов
def edit_post(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == 'GET':
      context = {'form':PostForm(instance=post),'id':id}
      return render(request, 'post_confirm_delete.html',context)
  elif request.method == 'POST':
    form = PostForm(request.POST, instance = post)
    if form.is_valid():
      form.save()
      messages.success(request, "The post has been updated successfully")
      return redirect("home")

 




class RegisterView(FormView):
  template_name = 'register.html'
  form_class = RegisterForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('home')
  #Проверка валидности
  def form_valid(self, form):
    user = form.save()
    if user:
      login(self.request, user)

    return super(RegisterView, self).form_valid(form)
#Авторизация    
def sign_in(request):
    if request.method =="GET":
        if request.user.is_authenticated:
          return redirect("home")
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f' {username.title()} Welcome back!')
                return redirect('home')
        return render(request, 'login.html', {'form': form})
#Выход
def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
  