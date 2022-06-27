from datetime import datetime
from django.db import models
from datetime import datetime, timedelta

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField(default=datetime.now().date())

    def __str__(self):
        return self.firstname


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.now().date())

    def __str__(self):
        return self.firstname

    