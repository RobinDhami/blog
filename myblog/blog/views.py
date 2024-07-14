from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from blog.models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful.')
            return redirect('profile')  # Redirect to profile page after login
        else:
            messages.error(request, 'Invalid username or password.')

    # If GET request or authentication failed, render the login form
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')
        location = request.POST.get('location')
        password = request.POST.get('password')

        # Basic validation
        if not (username and email and phone_number and password and bio and location and image):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        try:
            # Create a new User object
            user = User.objects.create_user(username=username, email=email, password=password)

            # Create a Blogger profile linked to the user
            blogger = Blogger.objects.create(
                user=user,
                name=username,
                email=email,
                phone=phone_number,
                bio=bio,
                image=image,
                location=location
            )

            messages.success(request, 'Account created successfully.')

            # Redirect to profile page after successful registration
            return redirect('profile')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('register')

    else:
        return render(request, 'register.html')