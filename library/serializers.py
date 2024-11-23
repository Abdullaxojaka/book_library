from rest_framework import serializers
from .models import Book, User, BorrowRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_available']


class BorrowRecordSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = BorrowRecord
        fields = ['id', 'user', 'book', 'borrowed_at', 'returned_at']


class BorrowBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
