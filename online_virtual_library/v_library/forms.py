from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class CategoryForm(ModelForm):
    class Meta:
        model = Category  
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author  
        fields = '__all__'

class LanguageForm(ModelForm):
    class Meta:
        model = Language  
        fields = '__all__'

class BookDocumentTypeForm(ModelForm):
    class Meta:
        model = BookDocumentType
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowedBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = '__all__'