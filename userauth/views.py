from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauth.models import User


# User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            # получаем имя пользвоателя из формы
            username = form.cleaned_data.get('username')
            # Созадем уведомление об успешной регистрации
            messages.success(request, f'Привет {username}, ваш аккаунт зарегистрирован!')
            # выполняем аутификацию
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password= form.cleaned_data['password1'])
            login(request, new_user)
            print(messages)
            # pip install django-email-verification
            return redirect('store:all_products')
    else:
        form = UserRegisterForm()
        print('form is not vailid')
    context = {
        'form': form,
    }
    return render(request, 'userauth/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('store:all_products')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # проверяем наличие email в базе данных
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Вы вошли в систему')
                return redirect('store:all_products')
        except:
            messages.warning(request, f'Пользователь {email} не существует')

        

    context = {

    }
    
    return render(request, 'userauth/sign-in.html', context)



def logout_view(request):
    logout(request)
    messages.success(request, f'Пользователь вышел из системы')
    return redirect( '/')

