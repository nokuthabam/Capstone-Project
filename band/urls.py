from django.urls import path, include, re_path
from . import views

app_name = 'band'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),

]
