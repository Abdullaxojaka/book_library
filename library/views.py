from rest_framework import viewsets, status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils import timezone
from .models import Book, User, BorrowRecord
from .serializers import (
    BookSerializer, UserSerializer, BorrowRecordSerializer, BorrowBookSerializer
)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class BorrowRecordViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = BorrowRecord.objects.filter(user=request.user)
        serializer = BorrowRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BorrowBookSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            book = Book.objects.filter(id=book_id, is_available=True).first()
            if book:
                BorrowRecord.objects.create(user=request.user, book=book)
                book.is_available = False
                book.save()
                return Response({"detail": "Book borrowed successfully"}, status=status.HTTP_201_CREATED)
            return Response({"detail": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def return_book(self, request, pk=None):
        record = BorrowRecord.objects.filter(id=pk, user=request.user, returned_at__isnull=True).first()
        if record:
            record.returned_at = timezone.now()
            record.book.is_available = True
            record.book.save()
            record.save()
            return Response({"detail": "Book returned successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid record"}, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ViewSet):
    """
    Users API with login endpoint.
    """

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        Custom login endpoint under users.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            # Token yoki boshqa autentifikatsiya ma’lumotlarini qaytarishingiz mumkin
            return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)