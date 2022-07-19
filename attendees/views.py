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

def index(request, pIndex=1):
    
    clist = Conference.objects
    mywhere = []
    kw = request.GET.get("keyword",None)
    if kw:
        clist = clist.filter(Q(name__contains=kw) | Q(start_time__contains=kw) | Q(end_time__contains=kw) | Q(location__contains=kw))
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
        aob = Conference.objects.all()[vo.id - 1].attendees.all()

        attendeelist = []
        for ao in Conference.objects.all()[vo.id - 1].attendees.all():
            attendeelist.append(ao.name)
        vo.attendeename = attendeelist

    context = {"conferencelist":list2, 'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    
    return render(request, "attendees/index/index.html",context)

# def index(request):
#     return render(request, 'attendees/index/index.html')

def login(request):
    return render(request, 'attendees/index/login.html')

def dologin(request):
    try:
        attendee = Attendees.objects.get(name=request.POST['name'])
        if attendee.stuid == request.POST['stuid']:
            request.session['attendeeuser'] = attendee.toDict()
            return redirect(reverse("attendees_index", args=[1]))
        else:
            context = {"info":"Invalid Student ID！"}

    except Exception as err:
        print(err)
        context = {"info":"Student not exists!"}
    return render(request, "attendees/index/login.html", context)

def logout(request):
    del request.session['attendeeuser']
    return redirect(reverse("attendees_login"))

