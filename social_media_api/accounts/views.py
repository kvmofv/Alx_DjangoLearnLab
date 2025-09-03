from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework import permissions
from . serializers import UserRegestrationSerializer, LoginSerializer, TokenSerializer
from .models import CustomUser


class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegestrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"message": "User created successfully. ", "username": user.username},
            status=status.HTTP_201_CREATED
        )
    
class LoginView(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data  # contains {"user": user, "token": token.key}
            return Response({
                "username": data["user"].username,
                "email": data["user"].email,
                "token": data["token"]
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenView(generics.GenericAPIView):
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
