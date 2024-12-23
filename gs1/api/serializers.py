from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'user', 'title', 'description', 'completed', 'due_date', 'created_at', 'updated_at']
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'title', 'description', 'completed', 'due_date', 'created_at', 'updated_at']
        fields = '__all__'
        # exclude=['user']