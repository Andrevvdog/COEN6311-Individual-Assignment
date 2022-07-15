from django.db import models
from datetime import datetime
from attendees.models import Attendees

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    attendees = models.ManyToManyField(Attendees)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id':self.id,'name':self.name,'location':self.location,'attendees':self.attendees,'start_time':self.start_time.strftime('%Y-%m-%d %H:%M:%S'),'end_time':self.end_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "conference"  # 更改表名