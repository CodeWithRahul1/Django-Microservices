from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserView, UserDetailView, UserListView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterUserView.as_view(), name='register-user'),
    path('api/user_details/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
]

