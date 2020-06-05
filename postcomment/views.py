'''from django.shortcuts import render
from rest_framework import viewsets          # add this
from postcomment.serializers import PostSerializer      # add this
from postcomment.models import Post                     # add this

class Post_View(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()'''

from django.shortcuts import render
from rest_framework import viewsets,status
from postcomment.serializers import PostSerializer   # add this
from postcomment.models import Post,UserPost

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
