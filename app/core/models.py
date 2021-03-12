from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):
    """Class to overirde BaseUserManager"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates user for the given arguments"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Customr user model to create a user using email id instead of
       username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
