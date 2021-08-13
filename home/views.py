from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
import time as t
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request): 
    return render(request,'home/home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)   
        
        # validation
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please Enter the valid details.')
        
        else:
            contact1=Contact(name=name,email=email,content=content) 
            contact1.save() 
            messages.success(request, 'Your message has been sent.')
            
        # if (phone)==int:
        #     contact1=Contact(name=name,email=email,phone=phone,content=content) 
        #     contact1.save() 
        #     messages.success(request, 'Your message has been sent222.')
        # else:
        #     messages.error(request, 'phone number must be in numeric form.')
            
        # #     contact1=Contact(name=name,email=email,phone=phone,content=content) 
        # #     contact1.save() 
        # #     messages.success(request, 'Your message has been sent222.')
            

    
    return render(request,'home/contact.html')


def about(request): 
    return render(request,'home/about.html')

def search(request): 
    query=request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        allpoststitle=Post.objects.filter(title__contains=query)
        allpostscontent=Post.objects.filter(content__contains=query)
        allpostsauthor=Post.objects.filter(content__contains=query)
        allposts=allpostscontent.union(allpostscontent,allpostsauthor)
    
    if allposts.count() == 0:
        messages.warning(request, 'Please search again with valid keyword.')
    params={'allposts': allposts,'query':query}
    return render(request,'home/search.html',params)

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        
        
    # check for errorneous input
    if len(username)<10:
        messages.error(request, "Your user name must be under 10 characters")
        return redirect('home')

    if not username.isalnum():
        messages.error(request, "User name should only contain letters and numbers")
        return redirect('home')
    if (pass1!= pass2):
            messages.error(request, "Passwords do not match")
            return redirect('home')

   
    myuser=User.objects.create_user(username,email,pass1)
    myuser.fname=fname
    myuser.lname=lname
    myuser.save()
    messages.success(request,'Your account has been created {{Users.username}}')
    t.sleep(2)
    return redirect('/')

  
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']    
        loginpass=request.POST['loginpass']    
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request,user)
            # messages.success(request,'{a}succefully log in.Welcome')
            messages.success(request,"succefully log in.Welcome")
            return redirect('/')
            
        else:
            messages.error(request,'Invalid Credentails, Please try again')
            return redirect('/')
    return HttpResponse('404- Not found')


          
def handlelogout(request):
    logout(request)
    messages.success(request,"succefully logged Out")
    return redirect('/')
    return HttpResponse('handlelogout')
    
    


        
    
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name= fname
        # myuser.last_name= lname
        # myuser.save()
        # messages.success(request, " Your account has been successfully created")
        # return render(request,'home/home.html')

