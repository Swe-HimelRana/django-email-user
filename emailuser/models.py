import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None,  username=None, **extra_fields):
        """ Creating and saving new user """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            """ Generating random unique username if not given """
            username = uuid.uuid4().hex[:12].upper()

        user = self.model(email=self.normalize_email(email),
                          username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username=None, **extra_fields):
        """ Create and saves a new superuser """

        user = self.create_user(
            email=email, password=password, username=username)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that support email instent of username """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
