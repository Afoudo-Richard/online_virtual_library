
from django.db import models

# Create your models here.


class Institution(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

# class UserType(models.Model):
#     type = models.CharField(max_length=200)

#     def __str__(self) -> str:
#         return self.type

# class User(models.Model):
#     institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     user_type = models.ManyToManyField(UserType)

#     def __str__(self) -> str:
#         return f"{self.firstname} {self.lastname}"


    

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
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    date_of_publication = models.DateField()
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)
    Language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    doc_type = models.ForeignKey(BookDocumentType, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author)

    