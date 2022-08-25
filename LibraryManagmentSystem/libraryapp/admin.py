from django.contrib import admin
from libraryapp.models import Admin,Library
#from .forms import AdminForm,LibraryForm


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display=['id','name','email','password','photo']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity','books']    
