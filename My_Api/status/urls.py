from django.urls import path
from .views import (
    StatusDetailUpdateDeleteAPIView,
    StatusListCreateView,
)


urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>', StatusDetailUpdateDeleteAPIView.as_view()),


]
