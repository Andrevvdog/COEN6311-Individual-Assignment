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
    clist = Conference.objects
    mywhere = []
    keyword = request.GET.get("keyword",None)
    if keyword:
        clist = clist.filter(Q(name__contains=keyword) | Q(start_time__contains=keyword) | Q(end_time__contains=keyword) | Q(location__contains=keyword))
        mywhere.append('keyword='+keyword)
    
    clist = clist.order_by("id")
    #Insert Pages
    pIndex = int(pIndex)
    page = Paginator(clist, 5)#5 conference per page
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list = page.page(pIndex)
    plist = page.page_range

    for vo in list:
        aob = Conference.objects.all()[vo.id - 1].attendees.all()

        attendeelist = []
        for ao in Conference.objects.all()[vo.id - 1].attendees.all():
            attendeelist.append(ao.name)
        vo.attendeename = attendeelist

    context = {"conferencelist":list, 'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    
    return render(request, "attendees/conference/viewconference.html",context)

def register(request, cid = 0):
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