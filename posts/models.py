from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Posts'
        
    # def __str__(self) -> str:
    #     return f"{self.title} by {self.user}"
        

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post File'
        verbose_name_plural = 'Post Files'
        db_table = 'Post Files'
        
    # def __str__(self) -> str:
    #     return f"{Post.title}'s file"
    
        
class Comment(models.Model):
    # one single post can have many comments
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'