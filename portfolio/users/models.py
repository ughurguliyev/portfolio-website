from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class UserManager(UserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, verbose_name='email', unique=True)
    username = models.EmailField(max_length=60, verbose_name='username', unique=True, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class GivenDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="device")
    device_model = models.CharField(max_length=100, verbose_name='Model of device')
    note = models.TextField(verbose_name="Note field", blank=True)

    def __str__(self):
        return self.device_model