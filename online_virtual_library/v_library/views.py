from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

from .decorators import *
from .forms import *

# Create your views here.


@unauthenticated_user
def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        try:
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('dashboard')

        except:
            messages.info(request, "Username or Password is incorrect")

        context = {
            'email': email,
            'password': password,
        }
    else:
        context = {
            'email': '',
            'password': '',
        }

    return render(request, 'v_library/index.html', context)

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "successfully created user " + username)
            return redirect('users')

    context = {
        'form': form
    }
    return render(request, 'v_library/register_user.html', context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required
@allowed_users(allowed_roles = ['staff'])
def users(request):
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'v_library/users.html', context)

@login_required
@admin_only
@allowed_users(allowed_roles = ['staff'])

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

def student_dashboard(request):

    users = User.objects.all()
    books = Book.objects.all()


    context = {
        'total_users': users.count(),
        'total_books': books.count(),
    }
    return render(request, 'v_library/student_dashboard.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'v_library/categories.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('categories')
        
    else:
        form = CategoryForm()

    context = {
        'title': "Add",
        'form': form,
    }
    return render(request, 'v_library/form/category_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories')
        
    else:
        form = CategoryForm(instance=category)
        
    context = {
        'title': "Edit",
        'form': form,
    }
    return render(request, 'v_library/form/category_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories')

@login_required
@allowed_users(allowed_roles = ['staff'])
def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'v_library/authors.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('authors')
        
    else:
        form = AuthorForm()

    context = {
        'title': "Add",
        'form': form,
    }
    return render(request, 'v_library/form/author_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST,instance=author)
        if form.is_valid():
            author = form.save()
            return redirect('authors')
        
    else:
        form = AuthorForm(instance=author)
        
    context = {
        'title': "Edit",
        'form': form,
    }
    return render(request, 'v_library/form/author_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('authors')


@login_required
@allowed_users(allowed_roles = ['staff'])
def languages(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'v_library/languages.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('languages')
        
    else:
        form = LanguageForm()

    context = {
        'title': "Add",
        'form': form,
    }
    return render(request, 'v_library/form/language_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_language(request, id):
    language = Language.objects.get(id=id)
    if request.method == 'POST':
        form = LanguageForm(request.POST,instance=language)
        if form.is_valid():
            language = form.save()
            return redirect('languages')
        
    else:
        form = LanguageForm(instance=language)
        
    context = {
        'title': "Edit",
        'form': form,
    }
    return render(request, 'v_library/form/language_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_language(request, id):
    author = Language.objects.get(id=id)
    author.delete()
    return redirect('languages')


@login_required
@allowed_users(allowed_roles = ['staff'])
def book_document_types(request):
    book_document_types = BookDocumentType.objects.all()
    context = {
        'book_document_types': book_document_types
    }
    return render(request, 'v_library/book_document_types.html', context)


@login_required
@allowed_users(allowed_roles = ['staff'])
def add_book_document_type(request):
    if request.method == 'POST':
        form = BookDocumentTypeForm(request.POST)
        if form.is_valid():
            book_document_type = form.save()
            return redirect('book_document_types')
    else:
        form = BookDocumentTypeForm()

    context = {
        'title': "Add",
        'form': form,
    }
    return render(request, 'v_library/form/book_document_type_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_book_document_type(request, id):
    book_document_type = BookDocumentType.objects.get(id=id)
    if request.method == 'POST':
        form = BookDocumentTypeForm(request.POST,instance=book_document_type)
        if form.is_valid():
            book_document_type = form.save()
            return redirect('book_document_types')
        
    else:
        form = BookDocumentTypeForm(instance=book_document_type)
        
    context = {
        'title': "Edit",
        'form': form,
    }
    return render(request, 'v_library/form/book_document_type_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_book_document_type(request, id):
    book_document_types = BookDocumentType.objects.get(id=id)
    book_document_types.delete()
    return redirect('book_document_types')


@login_required
@allowed_users(allowed_roles = ['staff'])
def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'v_library/books.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books')
    else:
        form = BookForm()

    context = {
        'title': "Add",
        'form': form,
    }
    return render(request, 'v_library/form/book_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('books')
        
    else:
        form = BookForm(instance=book)
        
    context = {
        'title': "Edit",
        'form': form,
    }
    return render(request, 'v_library/form/book_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')


# issued books section


@login_required
@allowed_users(allowed_roles = ['staff'])
def issued_books(request):
    borrowed_books = BorrowedBook.objects.all()
    context = {
        'borrowed_books': borrowed_books,
    }
    return render(request, 'v_library/issued_books.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def add_issued_book(request):
    if request.method == 'POST':
        form = BorrowedBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issued_books')
    else:
        form = BorrowedBookForm()

    context = {
        'title': "Issue",
        'form': form,
    }

    return render(request, 'v_library/form/issued_book_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def edit_issued_book(request, id):
    borrowed_book = BorrowedBook.objects.get(id=id)
    if request.method == 'POST':
        form = BorrowedBookForm(request.POST,instance=borrowed_book)
        if form.is_valid():
            form.save()
            return redirect('issued_books')
        
    else:
        form = BorrowedBookForm(instance=borrowed_book)
        
    context = {
        'title': "Edit Issued",
        'form': form,
    }
    return render(request, 'v_library/form/issued_book_form.html', context)

@login_required
@allowed_users(allowed_roles = ['staff'])
def delete_issued_book(request, id):
    borrowed_book = BorrowedBook.objects.get(id=id)
    borrowed_book.delete()
    return redirect('issued_books')

@login_required
@allowed_users(allowed_roles = ['student'])
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user = request.user)
    context = {
        'borrowed_books': borrowed_books,
    }
    return render(request, 'v_library/student_issued_books.html', context)

