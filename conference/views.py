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

def viewconference(request, pIndex=1):
    conference = Conference.objects

    mywhere = []
    keyword = request.GET.get("keyword",None)
    if keyword:
        conference = conference.filter(Q(start_date__contains=keyword) | Q(location__contains=keyword))
        mywhere.append('keyword='+keyword)
    
    conference = conference.order_by("id")
    datelist = []
    locationlist = []
    for vo in conference:
        if vo.start_date not in datelist:
            datelist.append(vo.start_date)
        if vo.location not in locationlist:
            locationlist.append(vo.location)

    #Insert Pages
    pIndex = int(pIndex)
    page = Paginator(conference, 5)#5 conference per page
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    conferencelist = page.page(pIndex)
    pagelist = page.page_range
    #Show the names of registered attendees
    for vo in conferencelist:
        attendeelist = []

        for ao in Conference.objects.all()[vo.id - 1].attendees.all():
            attendeelist.append(ao.name)
        vo.attendeename = attendeelist

    context = {"conferencelist":conferencelist,'datelist':datelist,'locationlist':locationlist,'pagelist':pagelist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    
    return render(request, "attendees/conference/viewconference.html",context)

def register(request, cid = 0):
    try:
        conference = Conference.objects.get(id=cid)
        attendees = Attendees.objects.get(name=(request.session['attendeeuser']['id']))

        conference.attendees.add(attendees)
        context = {'info':"Registered Successfully!"}
        return render(request, "attendees/info.html",context)

    except Exception as err:
        print(err)
        context = {'info':"Registered Fail!"}
        return render(request, "attendees/info.html",context)