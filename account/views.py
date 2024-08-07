from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

class SignupAPIView(APIView):
    def post(self, request):
        user = get_user_model().objects.create(
            username = request.data.get("username"),
            password = request.data.get("password"),
            nickname = request.data.get("nickname"),
        )
        if user.is_superuser:
            role = "superuser"
        elif user.is_staff:
            role = "staff"
        else:
            role = "user"
        return Response({
            "username": user.username,
            "nickname": user.nickname,
            "role": role
        })