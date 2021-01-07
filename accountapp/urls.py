from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="login"),
]
