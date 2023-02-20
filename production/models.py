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
    


class processalert(models.Model):
    id = models.AutoField(primary_key=True)
    furnace_name = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    started_at = models.CharField(max_length=100)
    cycle_number = models.CharField(max_length=100)
    process_name= models.CharField(max_length=100)
    process_limit= models.CharField(max_length=100)
    mailflag = models.CharField(max_length=100, default=False)
    exceeded = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    read = models.CharField(max_length=200,default=False)
    time = models.DateTimeField(auto_now=True)

class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    start_time = models.CharField(max_length=150, null=True, blank=True)
    end_time = models.CharField(max_length=150, null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Process(models.Model):
    id = models.AutoField(primary_key=True)
    ref_id = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    cycle_number = models.CharField(max_length=100)
    process_name = models.CharField(max_length=100)
    cam_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100, default="NA")
    min_temp = models.CharField(max_length=100, default="NA")
    max_temp = models.CharField(max_length=100, default="NA")
    spectro = models.CharField(max_length=100, default="NA")
    spectro_time = models.CharField(max_length=30, default="NA")
    power = models.CharField(max_length=30, default="NA")
    weight = models.CharField(max_length=30, default="NA")
    batch_status = models.CharField(max_length=50, default=False)
    cycle_flag = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "unique id: %s, Process: %s , Furnace: %s , Start: %s , End: %s , duration: %s" % (
            self.unique_id, self.process_name, self.cam_name, self.start_time, self.end_time, self.duration)
        
class Model_version(models.Model):
    model_name = models.CharField(max_length=100)
    weights_path = models.FileField()
    config_path = models.FileField()
    xml_path = models.FileField()

    def __str__(self):
        return self.model_name