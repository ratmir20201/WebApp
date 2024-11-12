from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView, UserRoomView

app_name = "registration"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("user_room/", UserRoomView.as_view(), name="user_room"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
