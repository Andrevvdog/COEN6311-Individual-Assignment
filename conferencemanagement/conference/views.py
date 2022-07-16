from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from attendees.models import Attendees
from conference.models import Conference
from events.models import Events
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import time

def register(request, cid = 0):
    '''加载详情表单'''
    try:
        cb = Conference.objects.get(id=cid)
        ab = Attendees.objects.get(name=(request.session['attendeeuser']['id']))

        cb.attendees.add(ab)
        context = {'info':"Registered Successfully!"}
        return render(request, "attendees/info.html",context)

    except Exception as err:
        print(err)
        context = {'info':"Registered Fail!"}
        return render(request, "attendees/info.html",context)