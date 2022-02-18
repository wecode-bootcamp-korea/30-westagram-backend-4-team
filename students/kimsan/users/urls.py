from django.urls import path
from users.views import UserView



urlpatterns = [
    path('/sign-up', UserView.as_view()),
]