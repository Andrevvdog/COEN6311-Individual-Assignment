from django.urls import path
from attendees import views as attendees
from conference import views as conference
from events import views as events

urlpatterns = [
    path('login', attendees.login, name = "attendees_login"),
    path('dologin', attendees.dologin, name = "attendees_dologin"),
    path('logout', attendees.logout, name = "attendees_logout"),

    path('conference/<int:pIndex>', conference.viewconference, name = "attendees_conference_viewconference"),
    path('conference/register/<int:cid>', conference.register, name = "attendees_conference_register"),

    path('events/<int:pIndex>', events.viewevents, name = "attendees_events_viewevents"),
]
