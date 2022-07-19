from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("ShopMiddleWare")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.path
        print("url: ", path)

        #管理后台是否登录
        urllist = ['/attendees/login', '/attendees/dologin', '/attendees/logout']
        if re.match(r'^/attendees', path) and (path not in urllist):
            if 'attendeeuser' not in request.session:
                return redirect(reverse("attendees_login"))


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response