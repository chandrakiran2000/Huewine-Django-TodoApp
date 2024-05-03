from django.db import models
from datetime import datetime

def get_current_date():
    return datetime.today().date()

# Create your models here.
class Task(models.Model):
    def __str__(self) :
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    priority = models.IntegerField()
    description = models.CharField(max_length=300, default="")
    status = models.CharField(max_length=100, default="pending")
    date = models.DateField(default=get_current_date)