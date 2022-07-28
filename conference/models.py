from django.db import models
from datetime import datetime
from attendees.models import Attendees

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    attendees = models.ManyToManyField(Attendees)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def toDict(self):
        return {'id':self.id,'name':self.name,'location':self.location,'attendees':self.attendees,'start_date':self.start_date,'end_date':self.end_date}

    class Meta:
        db_table = "conference" 