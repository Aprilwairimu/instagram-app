from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField (null=False, blank=False)
    image_name = models.CharField(max_length=100, null=False, blank=False)
    image_caption = models.CharField (max_length=100,null=False, blank=False)
    

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()


class Profile(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    profile =  models.ImageField (null=False, blank=False)
    Bio = models.TextField(max_length=100, null=False, blank=False)

    # def__str__(self):
    #     return self.name
        
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

class Comment(models.Model):
    author = models.CharField(max_length=100,null=False)
    comment = models.CharField(max_length=100, null=False, blank=False)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=False, blank=False )

class Likes(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    @classmethod
    def search_by_username(cls,search_term):
        gram = cls.objects.filter(username__icontains=search_term)
        return gramm