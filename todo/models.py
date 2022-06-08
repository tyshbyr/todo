from django.db import models

from customuser.models import User


class Task(models.Model):
    STATUS_CHOICES = (('Waiting', 'Ожидает'), ('In progress', 'Выполняется'), ('Completed', 'Заверешена'))
    
    title = models.CharField(verbose_name='Задача', max_length=100)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, blank=True)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Крайний срок', null=True, blank=True)
    date_of_completion = models.DateTimeField(verbose_name='Дата выполнения', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус выполнения', default='Waiting', max_length=35)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
        