
#from pyexpat import model
#from dataclasses import fields
#from pyexpat import model
from libraryapp.models import Admin,Library
from django import forms

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['id','name','email','password','photo']


class LibraryForm(forms.ModelForm):
    class Meta:
        model=Library
        fields=['id','name','quantity','books']
        #fields='__all__'
       

       