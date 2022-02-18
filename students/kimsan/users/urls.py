from django.urls import path
from users.views import UserView

#cd westagram/30-westagram-backend-4-team/students/kimsan

urlpatterns = [
    path('/sign-up', UserView.as_view()),
]