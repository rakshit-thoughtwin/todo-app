from django.shortcuts import render ,redirect ,HttpResponse, HttpResponseRedirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import TodoItem

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        user = User.objects.create_user(username=username, first_name=name, password=password)
        user.save()
        return redirect('login')
    return render(request,"signup.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"home.html")
        else:
            return HttpResponse("<b>not found</b>")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def home(request):

    if request.method == 'POST':
        todo_name = request.POST.get("new-todo")
        todo = TodoItem.objects.create(name=todo_name, user=request.user)
        return redirect("home")
    todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("-id")
    # todos = TodoItem.objects.all()
    return render(request, "home.html", {"todos": todos})

def update_todo(request, pk):
    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    todo.name = request.POST.get(f"todo_{pk}")
    todo.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))