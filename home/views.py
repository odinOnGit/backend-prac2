from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

  def delete(self, request, *args, **kwargs):
    BlogPost.objects.all().delete()
    return Response({'status' : 204})

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = 'pk'