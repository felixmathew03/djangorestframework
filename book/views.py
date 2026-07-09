from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Book
from .serializers import BookSerializer, UserRegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

def generate_token(user):
    refresh = RefreshToken.for_user(user)  # refresh, access
    return {
        "refresh":str(refresh),
        "access":str(refresh.access_token)
    }

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        print(serializer)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserViewSet(ViewSet):
    @action(detail=False, methods=['post'])
    def register(self,request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':"User registered successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False,methods=['post'])
    def login(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = generate_token(user)
            return Response({
                "message":"Login successfull",
                "refresh":tokens['refresh'],
                "access":tokens['access']
            })
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False,methods=['get'],permission_classes = [IsAuthenticated])
    def me(self,request):
        return Response({
            'message':'Welcome user'
        })
        
    @action(detail=False,methods=['post'],permission_classes = [IsAuthenticated])
    def logout(sel,request):
        refresh = request.data['refresh']
        token = RefreshToken(refresh)
        token.blacklist()
        return Response({
            "message":"Logged out"
        })
        
class PermissionDemoViewSet(ViewSet):
    @action(detail=False, methods=['get'], permission_classes = [AllowAny])
    def open_route(self,request):
        return Response({
            "message":"This is an open end point..."
        })
        
    @action(detail=False, methods=['get'], permission_classes = [IsAuthenticated])
    def logged_in_only(self,request):
        return Response({
            "message":"This is an end point open only for logged-in users..."
        })
    
    @action(detail=False, methods=['get','post'], permission_classes = [IsAuthenticatedOrReadOnly])
    def read_or_write(self,request):
        if request.method == 'GET':
            return Response({
                "message":"Anyone could read this end point..."
            })
        return Response({
            "message":"Only authenticated users could write data..."
        })
        
    @action(detail=False, methods=['get'], permission_classes = [IsAdminUser])
    def admin_only(self,request):
        return Response({
            "message":"This is an end point open only for admin user..."
        })