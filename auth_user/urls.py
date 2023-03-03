from django.urls import path
from .views import loginUser, logOutUser, signupUser

urlpatterns = [
    path("user/signup/",signupUser , name="signup"),
    path("user/login/",loginUser , name="login"),
    path("user/logout/",logOutUser , name="logout"),
]
