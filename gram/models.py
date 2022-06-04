from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField (null=False, blank=False)
    image_name = models.CharField(max_length=100, null=False, blank=False)
    image_caption = models.ImageField (null=False, blank=False)
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.ImageField (null=False, blank=False)
    comments = models.CharField(max_length=100, null=False, blank=False)

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
    comment = models.CharField(max_length=100, null=False, blank=False)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=False, blank=False )

    # @classmethod
    # def search_by_name(cls,search_term):
    #     gallery = cls.objects.filter(name__icontains=search_term)
    #     return search.html