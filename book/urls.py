from django.urls import path,include
from .views import BookViewSet, BookAPIView, UserViewSet, PermissionDemoViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books',BookViewSet)
router.register(r'auth',UserViewSet,basename='auth')
router.register(r"demo",PermissionDemoViewSet,basename='demo')
router.register(r"tasks",TaskViewSet, basename='tasks')

urlpatterns = [
    path('books-api/',BookAPIView.as_view()),
    path('',include(router.urls))
]

# http://127.0.0.1:8000/api/books       POST    -  Book is added to Book table
# http://127.0.0.1:8000/api/books       GET     -  All books from Book table is retreived
# http://127.0.0.1:8000/api/books/1/    GET     -  Book with id 1 is retreived
# http://127.0.0.1:8000/api/books/1/    PUT     -  Book with id 1 is updated fully
# http://127.0.0.1:8000/api/books/1/    PATCH   -  Book with id 1 is updated partially
# http://127.0.0.1:8000/api/books/1/    DELETE  -  Book with id 1 is removed

# http://127.0.0.1:8000/api/auth/register POST  - Signing up a user

# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MzU4MTg5NCwiaWF0IjoxNzgzNDk1NDk0LCJqdGkiOiIzNmIxY2RkYjUzNGY0MzZkYWUxMTZlYmRkZTJiOTEyMCIsInVzZXJfaWQiOiIxIn0.z65XDCziTppL9IP8DHYLNAyKOJkpbYW-AqpVaPCj9uw",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgzNDk1Nzk0LCJpYXQiOjE3ODM0OTU0OTQsImp0aSI6IjQ3YzlkZjJmODRmOTQ0YTk4NzBiY2ZhYWRkNDc4MmUyIiwidXNlcl9pZCI6IjEifQ.pGFIlm-TPlI6vIQOiVj3sEgTglKnksaFNJm7f5m0xTE"