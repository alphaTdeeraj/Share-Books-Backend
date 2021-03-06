from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
#importing function from helper
from .helpers import validatePhoneNum

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        print('entered the create user method')
        print('='*20)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(blank=False,null=False, unique=True)
    college = models.CharField(max_length=20,blank=False, null=False)
    contact_num = models.PositiveIntegerField(blank=False, null=False ,validators=[validatePhoneNum], unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['college','contact_num']

    objects = UserManager()

    def __str__(self):
        return self.email
        

class College(models.Model):
    name =  models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name
        

#presave method to upper case the college name
@receiver(pre_save ,sender=User)
def capitalizeCollegeName(instance, *args, **kwargs):
    instance.college = instance.college.upper()
    
    if not (College.objects.filter(name=instance.college)):
        College.objects.create(name=instance.college)
    return
