from django.db import models
from datetime import datetime
from django.db import models
from datetime import datetime
from conference.models import Conference

class Events(models.Model):
    conference = models.ForeignKey(Conference,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id':self.id, 'conference_id': self.conference,'name':self.name,'room':self.room,'speaker':self.speaker,'start_time':self.start_time.strftime('%Y-%m-%d %H:%M:%S'),'end_time':self.end_time.strftime('%Y-%m-%d %H:%M:%S')}
    
    class Meta:
        db_table = "events"
