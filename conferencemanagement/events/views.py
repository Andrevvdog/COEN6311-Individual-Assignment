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

def index(request, pIndex=1):
    '''浏览信息'''
    cid = request.GET.get("cid",1)
    conf = Conference.objects.filter(id=cid,attendees=(Attendees.objects.get(name=(request.session['attendeeuser']['id'])).id))

    if len(conf) != 0:
        cmod = Events.objects
        clist = cmod.filter(conference_id=cid)
        mywhere = []
        #获取并判断搜索条件
        kw = request.GET.get("keyword",None)
        if kw:
            clist = clist.filter(Q(name__contains=kw) | Q(start_time__contains=kw) | Q(start_time__contains=kw))
            mywhere.append('keyword='+kw)
        
        clist = clist.order_by("id")
        #Insert Pages
        pIndex = int(pIndex)
        page = Paginator(clist, 5)#5 conference per page
        maxpages = page.num_pages
        if pIndex > maxpages:
            pIndex = maxpages
        if pIndex < 1:
            pIndex = 1
        list2 = page.page(pIndex)
        plist = page.page_range

        for vo in list2:
            cob = Conference.objects.get(id=vo.conference_id)
            vo.conferencename = cob.name

        context = {"eventslist":list2, 'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
        
        return render(request, "attendees/events/index.html",context)
    
    else:
        context = {'info':"Please Register the Conference First!"}
        return render(request, "attendees/info.html",context)