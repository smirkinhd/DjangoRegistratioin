from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный email или пароль.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration_app/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно создан! Войдите в систему.')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте данные.')
    else:
        form = RegistrationForm()
    return render(request, 'registration_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'registration_app/home.html', {})