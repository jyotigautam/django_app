# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import Http404

from restapp.serializers import EventSerializer,ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework import authentication, permissions
from .models import Post,Events,Client

import logging 


class EventViewSet(APIView):

    def get(self, request, format=None):
      events = Events.objects.all()
      serializer = EventSerializer(events, many=True)
      return Response(serializer.data)
    

    def post(self, request, format=None):
      serializer = EventSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save(data_id=123)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientList(APIView):
  """
  List all clients, or create a new user.
  """

  def get(self, request, format=None):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
      serializer = ClientSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      clients.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

class ClientDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk): #Returns the single object that this view will display.
        try:
            return Client.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):#https://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
        #return Response(status=status.HTTP_204_NO_CONTENT)
