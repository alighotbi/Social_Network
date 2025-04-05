from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.core.validators import MinLengthValidator

from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=50,
        validators = [UniqueValidator(queryset=Post.objects.all()),
                     MinLengthValidator(3, message="Title must be at least 3 characters long.")
        ]
    )
        
    class Meta:
        model = Post
        exclude = ('created_time', 'updated_time')
        read_only_fields = ('user', )
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')
        read_only_fields = ('post', 'user')
        
        
class LikeSerializer(serializers.ModelSerializer):
    is_liked = serializers.BooleanField(required=False)
    class Meta:
        model = Like
        fields = ('post', 'user', 'is_liked')
        read_only_fields = ('post', 'user')