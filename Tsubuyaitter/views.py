from typing import Text
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404
from managers.models import Room
from Tsubuyaitter.models import Post
from django.shortcuts import redirect
# sign up
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import loader
#login require
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tsubuyaitter/signup.html', {'form': form})

# Create your views here.
@login_required
def index(request):
    context = {
        "rooms": Room.objects.all()
    }
    return render(request, 'tsubuyaitter/index.html', context)

@login_required
def room(request, room_id):
    if request.method == 'POST':
        room = Room.objects.get(pk=room_id)
        post = Post(
            text=request.POST['text'],
            posted_room=room,
            owner=request.user,
            is_solved=False,
        )
        post.save()
        return redirect('room', room_id=room_id)

    try:
        posts = Post.objects.filter(posted_room=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    context = {
        'posts': posts,
        'room_id': room_id,
        'that_room': Room.objects.get(pk=room_id),
    }
    return render(request, 'tsubuyaitter/room.html',context)


@login_required
def home(request):
    contents = {
        # 'usernames':User.objects.order_by('-id'),
        'rooms':Room.objects.order_by('-created_at')
    }
    return render(request, 'tsubuyaitter/home.html', contents)

@login_required
def resolved(request, post_id):
    that_post = Post.objects.get(pk=post_id)
    that_post.is_solved = True
    that_post.save()

    r_id = that_post.posted_room.id
    return redirect('room', room_id=r_id)

@login_required
def delete_post(request, post_id):
    that_post = Post.objects.get(pk=post_id)
    r_id = that_post.posted_room.id
    that_post.delete()

    return redirect('room', room_id=r_id)