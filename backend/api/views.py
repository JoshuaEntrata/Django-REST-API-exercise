from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

class BlogPostList(APIView):
    def get(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogPostCreate(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
class BlogPostUpdate(generics.RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk" 
    
class BlogPostDelete(generics.RetrieveDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk" 

class BlogPostFilteredList(APIView):
    def get(self, request, title):
        blog_posts = BlogPost.objects.filter(title__icontains=title)
            
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
