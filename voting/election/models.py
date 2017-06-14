from django.db import models
from user.models import User
from user.models import Group
# Create your models here.


class Election(models.Model):

    STATUS_CHOICES =(
        (0, 'Open'),
        (1, 'Close'),
        (2, 'Canceled'),
        (3, 'Disqualified ')
    )
    name = models.CharField(max_length=255) #default 5
    description = models.TextField(max_length=512) #default 1?

    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    group = models.ForeignKey(Group)
    #include the ballot and the election choices

class ElectionChoices(models.Model):

    election = models.ForeignKey(Election)  # specify model
    optionName = models.CharField(max_length=255) 


class Vote(models.Model):
   user = models.ForeignKey(User) # - do we really need that?
   electionChoice = models.ForeignKey(ElectionChoices)



