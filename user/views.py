from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import  User
from django.core.paginator import Paginator, Page

def index(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'LoggedIn successfully.')
            return redirect('home')  # Redirect to the dashboard after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    user = request.user
    if user.status and user.roles.all():
        users = User.objects.all()
        items_per_page = 5
        paginator = Paginator(users, items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'dashboard.html',{"data":page})
    else:
        messages.info(request, 'either user is not active or role not assigned')
        return redirect("home")
