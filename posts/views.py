from rest_framework import status

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post, PostFile
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

class PostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk, user=request.user)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PostListView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    
    # def get_post(self, post_pk):
    #     post = get_object_or_404(Post, pk=post_pk)
    
    def get(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
         
         
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        likes = post.likes.filter(is_liked=True).count()
        return Response({'likes':likes})
    
    
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LikeSerializer(serializer.data)
        if serializer.is_valid():
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        