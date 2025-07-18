from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase, TokenRefreshView

from generics.utils import send_message
from apps.user.serializers import RegisterUserSerializer, MyTokenObtainPairSerializer, RefreshSerializer
from rest_framework.views import APIView

from apps.user.tasks import send_message_register

User = get_user_model()


class RegisterUserAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            full_name = serializer.validated_data.get("full_name")

            user = User(email=email, full_name=full_name)
            user.set_password(password)
            user.save()

            try:
                send_message_register.delay(user.email, user.id)
            except Exception as e:
                print(f"Ошибка при отправке Celery-задачи: {e}")

            return Response({
                "id": user.id,
                "email": user.email,
                "message": "Регистрация успешна. Подтвердите почту.",
            })


class ActivateAPIView(APIView):
    permission_classes = []
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user.is_active= True
        user.save()
        return Response(True)


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = RefreshSerializer
