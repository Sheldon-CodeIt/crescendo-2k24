from django.urls import path
from .views import logout, RegisterPage, loginView, registerView


urlpatterns = [
    # path('register/', RegisterPage.as_view(), name="register"),
    # path('login/', CustomLoginView.as_view(), name="login"),
    path('login/', loginView, name="login"),
    path('register/', registerView, name="register"),
    path('logout/', logout, name="logout"),
]