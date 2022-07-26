from django.db import models
from datetime import datetime
from attendees.models import Attendees

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    attendees = models.ManyToManyField(Attendees)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def toDict(self):
        return {'id':self.id,'name':self.name,'location':self.location,'attendees':self.attendees,'start_time':self.start_time,'end_time':self.end_time}

    class Meta:
        db_table = "conference" 