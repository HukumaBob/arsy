from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from .serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
