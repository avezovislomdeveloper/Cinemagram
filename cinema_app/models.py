from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    

class Movies(models.Model):
    movie = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    images = models.ImageField(upload_to='media/')
    like = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    
    
    def average_rating(self):
        avg_rating = self.ratings.aggregate(Avg('score'))['score__avg']
        return avg_rating if avg_rating else 'Not rated'
    def __str__(self):
        return self.name
    


class Comment(models.Model):
    movie = models.ForeignKey(Movies, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'commented by {self.user}'
    

class Rating(models.Model):
    movie = models.ForeignKey(Movies, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])
    
    class Meta:
        unique_together = ('movie', 'user')
        