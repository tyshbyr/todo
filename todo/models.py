from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import User


class Task(models.Model):
    STATUS_CHOICES = (('Waiting', 'Ожидает'), ('In progress', 'Выполняется'), ('Completed', 'Заверешена'))
    
    title = models.CharField(verbose_name='Задача', max_length=100)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, blank=True)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Крайний срок', null=True, blank=True)
    date_of_completion = models.DateTimeField(verbose_name='Дата выполнения', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус выполнения', default='Waiting', max_length=35)

    def short_description(self):
        return self.description[:100]
    
    def get_absolute_url(self):
        return reverse("todo:update", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if self.status == 'Completed':
            self.date_of_completion = timezone.now()
        else:
            self.date_of_completion = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
        