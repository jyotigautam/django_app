# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import Http404

from restapp.serializers import UserSerializer,PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework import authentication, permissions
from .models import Post

import logging 

class UserList(APIView):
  """
  List all users, or create a new user.
  """

  def get(self, request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      users.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk): #Returns the single object that this view will display.
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):#https://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostViewSet(APIView):

    def get(self, request, format=None):
      posts = Post.objects.all()
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data)

    def post(self, request, format=None):
      serializer = PostSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk): #Returns the single object that this view will display.
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):#https://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)