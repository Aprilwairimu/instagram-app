from django.contrib import admin

# Register your models here.
from .models import Image,Profile,Comment,Follow,Like
    

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)