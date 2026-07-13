from rest_framework import serializers
from .models import Book, Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email']
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only= True)
    
    def validate(self, data):
        user  = authenticate(
            username = data['username'],
            password = data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        data['user'] = user
        return data
    
class TaskSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']