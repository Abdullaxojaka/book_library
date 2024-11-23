from django.contrib import admin
from .models import User, Book, BorrowRecord

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BorrowRecord)
