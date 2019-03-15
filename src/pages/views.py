from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import PostForm
from pastes.models import Paste
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
import uuid

def home_view(request, *args, **kwargs):
    if request.method == 'POST' and request.user.is_authenticated and not request.user.is_staff:
        form2 = PostForm(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.poster = request.user
            rand = str(uuid.uuid4())[:6]
            while Paste.objects.filter(generated_url=rand).exists():
                rand = str(uuid.uuid4())[:6]
            post.generated_url = rand
            post.save()
            return HttpResponseRedirect(reverse('detail', args=(post.generated_url,)))
    else:
        form2 = PostForm()
    q = request.GET.get("q")
    if q:
        pastes=Paste.objects.filter(Q(public=True) & Q(title__icontains=q)).order_by("-timestamp")
    else:
        pastes=Paste.objects.filter(public=True).order_by("-timestamp")[0:10]
    return render(request, "home.html", {'form2': form2, "pastes": pastes})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def detail_view(request, custom_uuid):
    post = get_object_or_404(Paste, generated_url=custom_uuid)
    return render(request, "paste_detail.html", {'post': post})

def edit_view(request, custom_uuid):
    post = get_object_or_404(Paste, generated_url=custom_uuid)
    if request.method == 'POST' and request.user.is_authenticated:
        form2 = PostForm(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.poster = request.user
            rand = str(uuid.uuid4())[:6]
            while Paste.objects.filter(generated_url=rand).exists():
                rand = str(uuid.uuid4())[:6]
            post.generated_url = rand
            post.save()
            return HttpResponseRedirect(reverse('detail', args=(post.generated_url,)))
    else:
        form2 = PostForm(instance=post)

    return render(request, "edit_paste.html", {"form2": form2, "post": post})

def paste_list_view(request, *args, **kwargs):
    if request.method=="POST":
        Paste.objects.filter(id__in=request.POST.getlist("id[]")).delete()
        return redirect(reverse("paste_list"))
    else:
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
