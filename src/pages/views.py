from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from pastes.models import Paste
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    if request.method == 'POST':
        form2 = PostForm(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.poster = request.user
            post.content = form2.cleaned_data.get('content')
            post.title = form2.cleaned_data.get('title')
            post.syntax = form2.cleaned_data.get('syntax')
            post.public = form2.cleaned_data.get('public')
            form2.save()
    else:
        form2 = PostForm()
    return render(request, "home.html", {'form2': form2})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4342, 1252]
    }
    return render(request, "about.html", my_context)

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def paste_list_view(request, *args, **kwargs):
    userposts = Paste.objects.filter(poster=request.user.id)

    if request.user.is_authenticated:
            user_posts_html = {'userposts': userposts}
    return render(request, "paste_list.html", user_posts_html)
