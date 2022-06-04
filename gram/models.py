from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField (null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.ImageField (null=False, blank=False)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.ImageField (null=False, blank=False)
    comments = models.CharField(max_length=100, null=False, blank=False)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()


class Profile(models.Model):
    # Profile = 
    Bio = models.CharField(max_length=100, null=False, blank=False)

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    @classmethod
    def search_by_name(cls,search_term):
        gallery = cls.objects.filter(name__icontains=search_term)
        return search.html