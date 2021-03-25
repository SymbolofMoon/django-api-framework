from django.urls import path
from .views import RegisterView,LoginView #import RegisterView and LoginView

#Here 2 views are used for 2 different urls onee for registration and other for login

urlpatterns = [
    

    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]