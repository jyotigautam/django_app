from django.contrib.auth.models import User

from rest_framework import serializers
from restapp.models import Events,Post,Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created', 'title', 'content')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','title', 'data_id','content')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','name','contactEmail', 'contactPhone','contactPerson')
