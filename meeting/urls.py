from django.urls import path
from . import views

urlpatterns = [
    path('meeting/', views.index, name='aql-meetups'),
    path('meeting/<slug:meetup_slug>/', views.meetup_detail, name='meetup_detail')
]