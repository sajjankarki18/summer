from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Photo(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)
    
    def imageURL(self):
        url = ''
        
        try:
            url = self.image.url
        except:
            url = ''
        
        return url    
    
    def __str__(self) -> str:
        return self.description    
    
@receiver(post_delete, sender=Photo)
def delete_category_if_no_photos(sender, instance, **kwargs):
    category = instance.category
    if category and not Photo.objects.filter(category=category).exists():
        category.delete()
        