from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

class RegisterForm(UserCreationForm):
  email = forms.EmailField(max_length=254)

  class Meta:
    model = User
    fields = (
        'username',
        'email',
        'password1',
        'password2',
    )
class PostForm(ModelForm):
  class Meta:
      model = Post
      fields = ('title', 'content','author','author')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)