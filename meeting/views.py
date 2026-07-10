from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'Los Angeles', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meeting/index.html', {
        'show_meetups': False,
        'meetups': meetups
    })    
    
def meetup_detail(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is a first meetup!',
    }
    return render(request, 'meeting/meetup-details.html', {
        'meetup_tittle': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
    