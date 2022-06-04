from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Имейл', max_length=255, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=128)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_admin = models.BooleanField(default=False, verbose_name='Админ')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
