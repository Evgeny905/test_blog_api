from django.urls import path, include
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
    path('api-auth/', include('rest_framework.urls')),
]
