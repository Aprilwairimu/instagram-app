from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Image(models.Model):
    image = models.ImageField ( upload_to='pictures/',null=True, blank=True)
    image_name = models.CharField(max_length=100, null=True, blank=True)
    image_caption = models.CharField (max_length=100,null=True, blank=True)
    

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()


class Profile(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    profile =  models.ImageField (null=True, blank=True)
    Bio = models.TextField(max_length=100, null=True, blank=True)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.profile.save()
    # def__str__(self):
    #     return self.name
        
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

class Comment(models.Model):
    author = models.CharField(max_length=100,null=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True, blank=True)
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following= models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    @classmethod
    def search_by_username(cls,search_term):
        gram = cls.objects.filter(username__icontains=search_term)
        return gramm