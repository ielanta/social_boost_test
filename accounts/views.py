from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions

from accounts.models import Account, User
from accounts.serializers import AccountSerializer, UserSerializer


class AccountList(generics.ListAPIView):
    """
    List all accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
