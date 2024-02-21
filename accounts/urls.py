from django.urls import path
from .views import CustomLoginView, logout, RegisterPage


urlpatterns = [
    path('register/', RegisterPage.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', logout, name="logout"),
]