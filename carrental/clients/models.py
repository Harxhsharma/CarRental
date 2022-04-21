from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Rent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carnumber = models.CharField(max_length=100,default="No")
    fromm = models.DateField(default=datetime.date.today)
    to=models.DateField(default=datetime.date.today)
    bookedcar=models.CharField(max_length=100,default="No")

    def __str__(self):
        return self.user.username
