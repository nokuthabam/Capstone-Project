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
    Render the signup page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
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
    Render the login page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
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
    Render the logout page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
    """
    logout(request)
    return redirect(reverse('band:index'))


#Band website views
def index(request):
    """
    Render the landing page for the band app (index.html).

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
    """
    return render(request, 'band/landing.html')


def home(request):
    """
    Render the home page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
    """
    return render(request, 'band/home.html')


def about(request):
    """
    Render the about page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest
    """
    return render(request, 'band/about.html')


def blog(request):
    """
    Render the blog page for the band app.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest

    :return: HttpResponse object
    :rtype: django.http.HttpResponse
    """
    #get all posts from database
    posts = Post.objects.all()

    #pass posts to template
    context = {
        'posts':posts
    }
    
    return render(request, 'band/blog.html', context)

