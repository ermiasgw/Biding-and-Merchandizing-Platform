from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'individual'),
        (2, 'organization'),
        (3, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    nationality = models.CharField(max_length=200)

    username=None
    first_name=None
    last_name=None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Individual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    identification_no = models.CharField(max_length=200)
    profile_picture = models.ImageField()

class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    website = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


