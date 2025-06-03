from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        label="Пароль"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}),
        label="Подтверждение пароля"
    )

    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'password']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Пароль должен содержать минимум 8 символов.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Пароль должен содержать минимум одну заглавную букву.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("Пароль должен содержать минимум одну цифру.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = UserProfile.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            last_name=self.cleaned_data['last_name'],
            first_name=self.cleaned_data['first_name'],
            middle_name=self.cleaned_data.get('middle_name', '')
        )
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        label="Пароль"
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            raise forms.ValidationError("Введите корректный email-адрес.")
        return username