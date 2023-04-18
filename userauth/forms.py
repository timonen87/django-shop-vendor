from django import forms

from django.contrib.auth.forms import UserCreationForm
from userauth.models import User



class UserRegisterForm(UserCreationForm):
    """
    Cоздаем класс регистарции пользователя,
    который насдедуется от класса орм Django UserCreationForm
    класс User передается  модели приложения userauth
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите свое имя','class': 'form-control',}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Введите свой email', 'class':'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Придумать пароль', 'class':'form-control'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Подтвердить пароль', 'class':'form-control'}))

    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']