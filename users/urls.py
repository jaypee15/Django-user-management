from django.urls import path, include
from users.views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]