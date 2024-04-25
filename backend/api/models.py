from django.db import models

class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('NEWS', 'News'),
        ('OPINION', 'Opinion'),
        ('TECH', 'Technology'),
        ('LIFE', 'Life'),
        ('SPORTS', 'Sports'),
        ('RANDOM', 'Random'),
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICES, default='RANDOM')
    
    def __str__(self):
        return self.title
    

