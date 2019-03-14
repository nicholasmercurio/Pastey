from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from pastes.models import Paste
from django.urls import reverse

import uuid
# Create your views here.
def home_view(request, *args, **kwargs):

    if request.method == 'POST':
        form2 = PostForm(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.poster = request.user
            post.save()
            #post.content = form2.cleaned_data.get('content')
            #post.title = form2.cleaned_data.get('title')
            #post.syntax = form2.cleaned_data.get('syntax')
            #post.public = form2.cleaned_data.get('public')
            rand = str(uuid.uuid4())[:6]
            while Paste.objects.filter(generated_url=rand):
                rand = str(uuid.uuid4())[:6]
            post.generated_url = rand
            #form2.save()
        #    context = {
        #        "poster_name": post.poster,
        #        "paste_contents": post.content,
        #        "paste_title": post.title,
        #        "paste_syntax": post.syntax,
        #        "paste_visible": post.public
        #    }
        #    return HttpResponseRedirect(reverse('details', args=(post.generated_url,)), context)
            return redirect('detail', pk=post.pk)
    else:
        form2 = PostForm()

    return render(request, "home.html", {'form2': form2})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", my_context)

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def detail_view(request, pk):

#    if request.user.is_authenticated:
#        if request.method=='POST':
#            form3 = PostForm(request.POST)
#            url = form3.generated_url
#            your_posts = Paste.objects.get(url)
#            context = {
#                'form3': form3
#            }
#            return render(request, "paste_detail.html", context)
    post = get_object_or_404(Paste, pk=pk)
    return render(request, "paste_detail.html", {'post': post})
    #return render(request, "paste_detail.html", {'form3': form3})

def paste_list_view(request, *args, **kwargs):
    userposts = Paste.objects.filter(poster=request.user.id)

    if request.user.is_authenticated:
            user_posts_html = {'userposts': userposts}
    return render(request, "paste_list.html", user_posts_html)

def top10_view(request, *args, **kwargs):
    if(public):
        obj = Paste.objects.get(id=1)
        context = {
            'title': obj.title,
            'poster': obj.poster,
            'content': obj.content,
        }
    return render(request, "home.html", context)
