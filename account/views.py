from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from account.models import Role, UserRole

class SignupAPIView(APIView):
    def post(self, request):
        user = get_user_model().objects.create(
            username = request.data.get("username"),
            password = request.data.get("password"),
            nickname = request.data.get("nickname"),
        )
        role, created = Role.objects.get_or_create(role='USER')
        UserRole.objects.create(user=user, user_role=role)
        user_roles = UserRole.objects.filter(user=user)
        return Response({
            "username": user.username,
            "nickname": user.nickname,
            "roles": [{'role': user_role.user_role.role} for user_role in user_roles],
        })