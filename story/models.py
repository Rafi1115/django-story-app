from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    detail = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    thumbnail = models.ImageField()
    detail = models.TextField()
    featured = models.BooleanField(default=True)
    # post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('post-category', args=[self.title])
    def get_absolute_url(self):
        return reverse('post-category', kwargs={
            'pk': self.pk
        })

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # def __str__(self):
    #     return str(self.thumbnail)
    
    def get_absolute_url(self):
        return reverse('post-recipe', kwargs={
            'pk': self.pk
        })
        
class Advertise(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    overview = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-advertise', kwargs={
            'pk': self.pk
        })

    
class FeaturedPost(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-featured', kwargs={
            'pk': self.pk
        })

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    featured = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #content = HTMLField()
    user = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })