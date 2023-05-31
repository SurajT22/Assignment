from django.shortcuts import render
from rest_framework import  permissions,authentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
# from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from .serializsers import UserSerializer,AuthTokenSerializer
# Create your views here.

class CreateUserView(CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """create a new authentication token for new user"""

    serializer_class = AuthTokenSerializer


class ManageUserView(RetrieveUpdateAPIView):
    """
    get
    patch
    put

    TODO - TOPIC (generic views RetriveUpdateView)
    https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdateapiview
    """

    serializer_class = UserSerializer

    # checking http header for authentication token  (authentication)
    authentication_classes = [authentication.TokenAuthentication]

    # allow users only when token is valid   (authorized)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):

        return self.request.user
