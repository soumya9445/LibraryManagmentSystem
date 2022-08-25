from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from LibraryManagmentSystem.libraryapp.models import Library
from libraryapp.models import Admin,Library
from libraryapp.forms import AdminForm,LibraryForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    return render(request,'index.html')

def signup(request):
    fm=AdminForm()
    return render(request,'signup.html',{'form':fm}) 
'''
def save(request):
    na=request. POST.get('t1') 
    em=request. POST.get('t2') 
    pas=request. POST.get('t3') 
    #img=request.FILES['t4']
    Admin(name=na,email=em,password=pas).save()
    messages.success(request,'SignUp Successfully')
    return redirect('signup') 
'''
def save(request):
    if request.method == 'POST':
        fm=AdminForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save() 
            messages.success(request,'SignUp Successfully')
            return redirect('signup')            

    else:
        fm=AdminForm()
    return render(request,'signup.html',{'form':fm})      

def login(request):
    return render(request,'login.html')  

def validate(request):
    em=request.POST.get('email')
    pas=request.POST.get('password')
    try:
        Admin.objects.get(email=em,password=pas)
        return redirect('addbooks')
    except Admin.DoesNotExist:
        messages.error(request,'Invalid User')
        #return render(request,'login.html',{'error_message':'Invalid User'}) 
        return redirect('login')   

class addbooks(SuccessMessageMixin,CreateView):
    template_name='books.html'
    model= Library
    form_class = LibraryForm
    #fields='__all__'
    success_url = '/addbooks/'   
    success_message='Book Upload Successfully!!'    

class allbook(ListView):
    template_name="allbook.html"
    model=Library
    form_class = LibraryForm

class Update( SuccessMessageMixin,UpdateView):
    template_name='update.html'
    model=Library
    form_class=LibraryForm
    success_url='/allbook/'
    success_message='Record Will Be Updated Successfully!!' 

class Delete( SuccessMessageMixin,DeleteView):
    template_name='delete.html'
    model=Library
    form_class = LibraryForm
    success_url='/allbook/'
    success_message='Record Will Be Deleted Successfully!!'       
        
