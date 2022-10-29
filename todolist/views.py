from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
import datetime
from todolist.forms import TaskForm
from django.contrib.auth.models import User
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def home_page(request) :
    task = Task.objects.all()
    form = TaskForm()
    if request.method == "POST" :
        user = request.POST['user']
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']

        user = User.objects.get(pk = user)
        Task.objects.create(
            user = user,
            title = title,
            date = date,
            description = description
        )       
    context = {
        "task" : task,
        "form"  : form
    }
    return render(request, "home_page.html", context)

def home_page_json(request) :
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_task_ajax(request) :
    if request.method == "POST" :
        user = request.POST['user']
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']

        user = User.objects.get(pk = user)
        Task.objects.create(
            user = user,
            title = title,
            date = date,
            description = description
        )
    return render(request, "create_task.html")


@login_required(login_url='/todolist/login/')
def create_task(request) :
    form = TaskForm()
    print("test")
    if request.method == "POST" :
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Task berhasil ditambahkan')
            return HttpResponseRedirect(reverse('todolist:home_page'))
    context = {
        "form" : form
    }
    return render(request, "create_task.html", context)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:home_page")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return HttpResponseRedirect(reverse('todolist:login_user'))
    
    context = {'form':form}
    return render(request, 'register.html', context)