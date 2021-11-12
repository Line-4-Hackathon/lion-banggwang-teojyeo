from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from datetime import datetime
from django.utils.dateformat import DateFormat

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30, unique=True, null=True)
    coin = models.IntegerField(default=10000000)    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class ToiletApp(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 100, default = '')
    mainphoto = models.FileField(blank=True, null=True, upload_to = 'imgs/')  
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ToiletApp, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)