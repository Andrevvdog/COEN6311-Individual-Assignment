from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from attendees.models import Attendees
from conference.models import Conference
from django.shortcuts import redirect
from django.urls import reverse
import re
from django.core.paginator import Paginator
from django.db.models import Q

def login(request):
    return render(request, 'attendees/index/login.html')

def dologin(request):
    try:
        attendee = Attendees.objects.get(name=request.POST['name'])
        if attendee.stuid == request.POST['stuid']:
            request.session['attendeeuser'] = attendee.toDict()
            request.session['cid'] = 0
            return redirect(reverse("attendees_conference_viewconference", args=[1]))
        else:
            context = {"info":"Invalid Student ID！"}

    except Exception as err:
        print(err)
        context = {"info":"Student not exists!"}
    return render(request, "attendees/index/login.html", context)

def logout(request):
    del request.session['attendeeuser']
    del request.session['cid'] 
    return redirect(reverse("attendees_login"))

