
# #后台管理子路由文件
from django.urls import path
from attendees.views import attendees
from conference.views import conference
from events.views import events

urlpatterns = [
    path('<int:pIndex>', attendees.index, name = "attendees_index"),

    path('login', attendees.login, name = "attendees_login"),
    path('dologin', attendees.dologin, name = "attendees_dologin"),
    path('logout', attendees.logout, name = "attendees_logout"),

    path('attendees/register/<int:cid>', conference.register, name = "attendees_conference_register"),

    path('events/<int:pIndex>', events.index, name = "attendees_events_index"),
]
