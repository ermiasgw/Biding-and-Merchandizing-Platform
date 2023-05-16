from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'individual'),
        (2, 'organization'),
        (3, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=128)
    phone_number = PhoneNumberField(blank=True)
    country = CountryField()

    username=None
    first_name=None
    last_name=None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Individual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    identification_no = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile-images/')

class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    category = models.ManyToManyField(Category)
    website = models.URLField()
    description = models.TextField()
    tin_no = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo-images/')

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()


