from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


LIST_MODULE_PERM = ['accounts', 'todo']
LIST_PERM = ['accounts.view_user', 'accounts.delete_user', 'todo.view_task',
                        'todo.add_task', 'todo.change_task', 'todo.delete_task']

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm):
        if self.is_active and self.is_superuser:
            return True
        return perm in LIST_PERM

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return app_label in LIST_MODULE_PERM
        
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
