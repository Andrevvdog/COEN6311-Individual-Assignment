from django.db import models
from datetime import datetime
from django.db import models
from datetime import datetime
from conference.models import Conference

class Events(models.Model):
    conference = models.ForeignKey(Conference,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    speaker = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def toDict(self):
        return {'id':self.id, 'conference_id': self.conference,'name':self.name,'room':self.room,'speaker':self.speaker,'start_time':self.start_time,'end_time':self.end_time,'start_date':self.start_date,'end_date':self.end_date}
    
    class Meta:
        db_table = "events"
