from django.shortcuts import render
from .models import Meeting
# Create your views here.

def index(request):
    meetups = Meeting.objects.all()
    return render(request, 'meeting/index.html', {
        'show_meetups': False,
        'meetups': meetups
    })    
    
def meetup_detail(request, meetup_slug):
    selected_meetup = Meeting.objects.get(slug=meetup_slug)
    return render(request, 'meeting/meetup-details.html', {
        'meetup_title': selected_meetup.title,
        'meetup_description': selected_meetup.description
    })
    