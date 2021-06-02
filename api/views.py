from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User


# Register API
class RegisterAPI(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication]
    
    #use tuple for more than one class e.g (IsAuthenticated, permissions.AllowAny)
    permission_classes = [permissions.AllowAny]

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class UserRecordAPI(APIView):
    
    permission_classes = [permissions.AllowAny]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


