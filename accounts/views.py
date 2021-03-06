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
    """
    Create User and Account
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
