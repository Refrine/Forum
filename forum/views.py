from django.shortcuts import render
from .models import Forum

rooms=[
    {'id': 1, 'name': 'p14'},
]


def home(request):
    rooms = Forum.objects.all()
    context = {'rooms': rooms}
    return render(request, 'forum/home.html', context)

def room(request, pk):
    room = Forum.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'forum/room.html', context)



