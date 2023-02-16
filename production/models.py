from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    Estimated_target = models.IntegerField(default="")
    Achieved_target = models.IntegerField(default="")
    Score = models.IntegerField(default="")
    Bonus = models.IntegerField(default="")
    Datetime = models.DateField(default="")
    Time = models.TimeField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data')
    
    