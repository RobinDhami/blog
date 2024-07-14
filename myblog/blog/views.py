from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_view(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username'],
        email = request.POST['email'],
        phone_number = request.POST['phone_number'],
        bio = request.POST['bio'],
        image= request.FILES.get['image'],
        location = request.POST['location']
        password = request.POST['password']
        if not(username and email and phone and password and bio and image and location):
            messages.error(request,"All the field are required")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already Exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect('register')
                
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            blogger = Blogger(
                user=user,
                name=username,  # You can adjust this based on your form design
                email=email,
                phone=phone_number,
                bio=bio,
                image=image,
                location=location
            )
            blogger.save()
            return redirect('profile')  # Replace 'profile' with your profile URL name
        except Exception as e:
            messages.error(request, str(e))
            return redirect('register')
    else:
        return render(request, 'register.html')