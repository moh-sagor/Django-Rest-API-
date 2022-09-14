from django.urls import path
from .views import (
    StatusDetailAPIView,
    StatusListCreateView,
)


urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>', StatusDetailAPIView.as_view()),


]
