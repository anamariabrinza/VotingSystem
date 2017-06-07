from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Group(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)


class User(AbstractUser):

    GENDER_CHOICES = (
        (0, ('Male')),
        (1, ('Female')),
    )

    ROLE_CHOICES = (
        (0, ('Student')),
        (1, ('Proffesor')),
        (2, ('Administration')),
        (3, ('ElectionComisioner'))

    )

    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    role = models.IntegerField(choices=ROLE_CHOICES, default=2)
    groups = models.ManyToManyField(Group)



