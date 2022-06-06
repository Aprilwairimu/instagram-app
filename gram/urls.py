from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home, name='home',),
    path('register',views.register, name='register',),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('post/',views.post_pic,name='post'),
    path('profile/',views.profile, name='profile',),
    path('comment/<str:pk>/', views.comment, name='comment'),
    path('image/<pk>/',views.ViewImage, name='image',),
    path('like/<str:pk>/', views.like, name='like_post'),
    path('search/',views.search_results, name='search',),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)