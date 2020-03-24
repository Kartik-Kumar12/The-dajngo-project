from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item,Order
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages 


# Create your views here.

# View for extraction of items from database

def home(request):
    
    items=Item.objects.all()
    paginator = Paginator(items,10)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)
  
    return render(request,'home.html',{ 'items':paged_items })

# View for registering

def sign_in(request):
  if request.method=='POST':
    first_name=request.POST['firstname']
    last_name=request.POST['lastname']
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['pass']
    conf_pass=request.POST['pass1']
    
    if password != conf_pass:
             messages.error(request,'Password not matching')
             return redirect('sign_in')       
    else:
        
        
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.save()
       
        messages.success(request,"You are registered succesfully")
        return redirect('log_in')
  else:
       return render(request,'sign.html')

# View for login

def log_in(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None :
           auth.login(request,user)
           messages.success(request,"You are logged in ")
           return redirect('/')

        else:
            messages.error(request,"Invalid credentials")
            return redirect('log_in')
    else:
        return render(request,'login.html')


# View for logging out 

def log_out(request):
    auth.logout(request)
    return redirect('/')

# View for ordering

def order(request, pk):
    if request.method=='POST':
        element=Order()
        element.user=request.user
        element.index = get_object_or_404(Item,id=pk)
        element.address=request.POST['address']
        element.locality=request.POST['town']
        element.pincode=request.POST['pincode']
        element.city=request.POST['city']
        element.state=request.POST['state']
        element.mob_no=request.POST['usr_tel']
        element.qty=request.POST['qty']
        element.save()
        return redirect('/')
        
    else:
       return render(request,'order.html')

# View for extraction of ordered items

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'my_orders.html',{'orders':orders})

# View for filtering items

def contact(request):
   return render(request,'contact.html')
