from django.shortcuts import render, redirect
from .models import Forum
from .forms import RoomForm



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


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
            
    context={'form': form}
    return render(request, 'forum/room_form.html', context)




def updateRoom(request, pk):
    room = Forum.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'forum/room_form.htnl', context)



def deleteRoom(request,pk):
    room = Forum.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    
    
    return render(request, 'forum/main.html', {'obj':room})
    



