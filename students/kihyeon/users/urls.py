from django.urls import path, include
from users.views import SignUpView, LoginView

urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("login", LoginView.as_view()),
]
