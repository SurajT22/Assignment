from . import views
from django.urls import path

urlpatterns = [
    path("user/create/", views.CreateUserView.as_view(), name="create"),
    path("user/token/", views.CreateTokenView.as_view(), name="token"),
    path("user/me/", views.ManageUserView.as_view(), name="me"),
]
