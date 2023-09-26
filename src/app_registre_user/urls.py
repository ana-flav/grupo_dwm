from django.urls import path

from .views import cadastro ,createUser

urlpatterns = [
    path("", cadastro, name="registre"),
    path("createUser/", createUser, name="createUser"),
]