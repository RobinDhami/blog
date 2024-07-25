from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from blog.models import *
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login/')
def profile(request):
    user_profile = Blogger.objects.get(user=request.user)
    user_posts = post.objects.filter(author=request.user)
    context={
        'user' : request.user,
        'profile': user_profile,
        'posts':user_posts
    }
    return render(request,'profile.html',context)

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

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return render(request,'home.html')

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

            messages.success(request, 'Account created successfully.')

            # Redirect to profile page after successful registration
            return redirect('profile')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('register')

    else:
        return render(request, 'register.html')


@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not title or not content:
            messages.error(request, 'Both title and content are required.')
        else:
            post.objects.create(
                title=title,
                content=content,
                author=request.user,
                created_at=timezone.now()
            )
            messages.success(request, 'Post created successfully.')
            return redirect('home')

    return render(request, 'create_post.html')

@login_required(login_url='/login/')
def page(request):
    posts = post.objects.all()
    paginator = Paginator(posts, 2)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request, 'posts.html', context)

@login_required(login_url='/login/')
def post_detail(request, id):
    post = get_object_or_404(post, id=id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

