from django.db import models
from datetime import datetime

# Create your models here.
class Attendees(models.Model):
    name = models.CharField(max_length = 255) 
    stuid = models.CharField(max_length = 255) 

    def toDict(self):
        return {'id':self.name,'stuid':self.stuid}

    class Meta:
        db_table = "attendees"
