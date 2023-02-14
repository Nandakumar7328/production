from django.db import models

class Data(models.Model):
    Estimated_target = models.IntegerField(default="")
    Achieved_target = models.IntegerField(default="")
    Score = models.IntegerField(default="")
    Bonus = models.IntegerField(default="")
    Datetime = models.DateField(default="")
    Time = models.TimeField(default="")
    
    