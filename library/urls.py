from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UsersViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'borrow', BorrowRecordViewSet, basename='borrow')

urlpatterns = [
    path('', include(router.urls)),
]
