from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home',),
    path('register',views.register, name='register',),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('post/',views.post_pic,name='post'),
    path('profile/',views.profile, name='profile',),
    path('search/',views.search_results, name='search',),
    
]