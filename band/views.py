from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post

# Create your views here.

#Authentication views
def signup(request):
    """
    This view will render the signup page.
    Parameters:
        request: HttpRequest object
    Returns:
        HttpResponse object
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('band:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def user_login(request):
    """
    This view will render the login page.
    Parameters:
        request: HttpRequest object
    Returns:
        HttpResponse object
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            #allow login and let user vote
            login(request, user)
            return redirect(reverse('band:home'))
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'registration/login.html')


def user_logout(request):
    """
    This view will render the logout page.
    Parameters:
        request: HttpRequest object
    Returns:
        HttpResponse object
    """
    logout(request)
    return redirect(reverse('band:index'))


#Band website views
def index(request):
    """
    This view renders the landing page for the band app.
    """
    return render(request, 'band/landing.html')


def home(request):
    """
    This view renders the home page for the band app.
    """
    return render(request, 'band/home.html')


def about(request):
    """
    This view renders the about page for the band app.
    """
    return render(request, 'band/about.html')


def blog(request):
    """
    This view renders the blog page for the band app.
    """
    #get all posts from database
    posts = Post.objects.all()

    #pass posts to template
    context = {
        'posts':posts
    }
    
    return render(request, 'band/blog.html', context)

