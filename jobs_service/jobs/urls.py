from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CreateJobView

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/create-job/', CreateJobView.as_view(), name='create-job'),
]

