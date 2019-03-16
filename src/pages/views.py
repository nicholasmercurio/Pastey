from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import PostForm, ShareForm
from pastes.models import Paste, get_paste
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
import uuid
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def home_view(request, *args, **kwargs):
    if request.method == 'POST' and request.user.is_authenticated and not request.user.is_staff:
        form2 = PostForm(request.POST)
        if form2.is_valid():
            try:  # If Paste OR User does not exist
                post = form2.save(commit=False)
            except ObjectDoesNotExist:
                raise Http404("Paste does not exist")
            post.poster = request.user
            rand = str(uuid.uuid4())[:6] # 6 digits
            while Paste.objects.filter(generated_url=rand).exists():
                rand = str(uuid.uuid4())[:6]
            post.generated_url = rand
            post.save()
            return HttpResponseRedirect(reverse('detail', args=(post.generated_url,)))
    else:
        form2 = PostForm()
    q = request.GET.get("q")
    if q:
        pastes=Paste.objects.filter(Q(public=True) & Q(title__icontains=q)).order_by("-timestamp") # queieres both,checks if both true, and orders by timestamp
    else:
        if request.user.is_authenticated:
            pastes=Paste.objects.filter(Q(public=True)|Q(shares=request.user)).order_by("-timestamp")[0:10] #quieres both, check if either true, orders by time stamp, 0 to 10 pastes
        else:
            pastes=Paste.objects.filter(public=True).order_by("-timestamp")[0:10]

    return render(request, "home.html", {'form2': form2, "pastes": pastes})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

@login_required
def detail_view(request, custom_uuid):
    try:
        post = get_paste(custom_uuid, request.user)
        return render(request, "paste_detail.html", {'post': post})
    except ObjectDoesNotExist:
        raise Http404("Paste does not exist")

@login_required
def share_view(request, custom_uuid):
    post = get_object_or_404(Paste.objects.filter(poster=request.user), generated_url=custom_uuid)
    if request.method == 'POST' and request.user.is_authenticated:
        form2 = ShareForm(request.POST)
        if form2.is_valid():
            value = form2.cleaned_data["username"]
            print(value)
            print(User.objects.filter(Q(username=value)|Q(email=value)))
            user = User.objects.filter(Q(username=value)|Q(email=value))[0]
            post.shares.add(user)
            post.save()
            return HttpResponseRedirect(reverse('detail', args=(post.generated_url,)))
    else:
        form2 = ShareForm()

    return render(request, "edit_paste.html", {"form2": form2, "post": post})

@login_required
def edit_view(request, custom_uuid):
    try:
        post = get_object_or_404(Paste, generated_url=custom_uuid) # If object not found, throws 404
    except ObjectDoesNotExist:
        raise Http404("Paste does not exist")
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

@login_required
def delete_confirm_view(request):
    return render(request, "delete_confirm.html", {})

@login_required
def delete_user(request):
    if request.user.is_authenticated:
        user = request.user
        user.is_active = False
        user.username = "deactivated"+str(user.pk)
        user.save()
        return redirect('home')
    else:
        return redirect('home')



@login_required
def paste_list_view(request, *args, **kwargs):
    if request.method=="POST":
        Paste.objects.filter(id__in=request.POST.getlist("id[]")).delete()
        return redirect(reverse("paste_list"))
    else:
        userposts = Paste.objects.filter(poster=request.user.id)
        if request.user.is_authenticated:
                user_posts_html = {'userposts': userposts}
        return render(request, "paste_list.html", user_posts_html)
