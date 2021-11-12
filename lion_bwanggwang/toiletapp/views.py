from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth 
from django.contrib.auth.models import User
from django.views.generic import FormView  
from .forms import PostSearchForm
from .models import ToiletApp
from django.utils import timezone
from .models import Comment

# Create your views here.
def main(request):
    return render(request, "main.html")

def main2(request):
    return render(request, "main2.html")

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password =request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('main')
        return render(request, "signup.html")
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def new(request):
    return render(request, 'new.html')

def create(request):
    new_toilet = ToiletApp()
    new_toilet.title = request.POST['title']
    new_toilet.writer = request.POST['writer']
    new_toilet.body = request.POST['body']
    new_toilet.mainphoto = request.FILES['imgs']
    new_toilet.pub_date = timezone.now()
    new_toilet.save()
    return redirect('review')

def review(request):
    revs = ToiletApp.objects.all()
    return render(request, 'review.html', {'revs': revs})

def detail(request):
    if request.method == "POST":
        comment = Comment()
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
        
    return render(request, 'detail.html')

def detail_com(request):
    coms= Comment.objects.all()
    return render(request, 'detail.html', {'coms':coms})

# def edit(request, id):
#     edit_rev = ToiletApp.objects.get(id = id)
#     return render(request, 'edit.html', {'rev':edit_rev})

# def update(request, id):
#     update_toilet = ToiletApp.objects.get(id = id)
#     update_toilet.title = request.POST['title']
#     update_toilet.writer = request.POST['writer']
#     update_toilet.body = request.POST['body']
#     update_toilet.pub_date = timezone.now()
#     update_toilet.save()
#     return redirect('detail', update_toilet.id)