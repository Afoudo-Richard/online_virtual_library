from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

from .decorators import *

# Create your views here.


@unauthenticated_user
def index(request):
    if request.method == "POST":
        print("Inside the post method here ..................")
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        print(email)
        print(password)
        if user is not None:
            username = user.username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("Inside user")
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or Password is incorrect")
        else:
            print("Could not find email")
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'v_library/index.html')

def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required
def users(request):
    return render(request, 'v_library/users.html')

@login_required
def dashboard(request):
    users = User.objects.all()
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {
        'total_users': users.count(),
        'total_books': books.count(),
        'total_categories': categories.count(),
        'total_authors' : authors.count(),
    }
    return render(request, 'v_library/dashboard.html', context)


@login_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'v_library/categories.html', context)

@login_required
def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'v_library/authors.html', context)