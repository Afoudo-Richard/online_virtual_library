
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Institution(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Library(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.firstname


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.language

class BookDocumentType(models.Model):
    doc_type = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.doc_type

class Category(models.Model):
    STATUS = (
        ("Active", "Active"),
        ('InActive', "InActive")
    )
    name = models.CharField(max_length=300)
    status = models.CharField(max_length=300, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    STATUS = (
        ("Active", "Active"),
        ('InActive', "InActive")
    )
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    date_of_publication = models.DateField()
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=300, choices=STATUS, default="Active")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    # library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    doc_type = models.ForeignKey(BookDocumentType, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return self.title

class BorrowedBook(models.Model):
    STATUS = (
        ("Issued", "Issued"),
        ('Returned', "Returned"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    date_issued = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=300, choices=STATUS, default="Issued")
    late_return_fee = models.IntegerField()