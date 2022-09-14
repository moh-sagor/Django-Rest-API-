from django.urls import path
from .views import (
    # StatusDetailUpdateDeleteAPIView,
    # StatusListCreateView,
    StatusViewset,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'status', StatusViewset, basename="status")

urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    # path('status/', StatusListCreateView.as_view()),
    # path('status/<id>', StatusDetailUpdateDeleteAPIView.as_view()),

]+router.urls
