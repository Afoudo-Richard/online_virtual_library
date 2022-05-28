from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Institution)
# admin.site.register(UserType)
# admin.site.register(User)
admin.site.register(Library)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(BookDocumentAssetType)
admin.site.register(Book)

