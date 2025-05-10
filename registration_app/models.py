from django.db import models
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию"
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите ваше имя"
    )
    middle_name = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        blank=True, 
        null=True,
        help_text="Введите ваше отчество (если есть)"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите ваш email адрес"
    )
    password = models.CharField(
        max_length=128,
        verbose_name="Пароль",
        help_text="Введите пароль"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        middle_name = self.middle_name if self.middle_name else ""
        return f"{self.last_name} {self.first_name} {middle_name}".strip()

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
        ordering = ['last_name', 'first_name']
