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

def viewevents(request, pIndex=1):
    cid = request.GET.get("cid",0)

    print(request.session['cid']) #Store the current conference id into the session in case that cid = 0 when filtering

    if cid != 0 and request.session['cid'] == '0':
        request.session['cid'] = str(cid)

    elif request.session['cid'] != '0' and cid != 0:
        request.session['cid'] = str(cid)
    
    elif request.session['cid'] != '0' and cid == 0:
        cid = int(request.session['cid'])

    else:
        context = {'info':"Unknown Error!"}
        return render(request, "attendees/info.html",context)

    
    conf = Conference.objects.filter(id=cid,attendees=(Attendees.objects.get(name=(request.session['attendeeuser']['id'])).id))

    if len(conf) != 0:
        cmod = Events.objects
        clist = cmod.filter(conference_id=cid)
        mywhere = []
        keyword = request.GET.get("keyword",None)
        if keyword:
            clist = clist.filter(Q(name__contains=keyword) | Q(start_time__contains=keyword) | Q(end_time__contains=keyword) | Q(room__contains=keyword))
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
            cob = Conference.objects.get(id=vo.conference_id)
            vo.conferencename = cob.name

        context = {"eventslist":list, 'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
        
        return render(request, "attendees/events/viewevents.html",context)
    
    else:
        context = {'info':"Please Register the Conference First!"}
        return render(request, "attendees/info.html",context)