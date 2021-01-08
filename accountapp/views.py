from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, SuggestionUserSerializer


User = get_user_model()


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]


class SuggestionListAPIView(ListAPIView):
    serializer_class = SuggestionUserSerializer

    def get_queryset(self):
        qs = User.objects.exclude(pk=self.request.user.pk)
        qs = qs.exclude(pk__in=self.request.user.following_set.all())
        return qs


# FIXME: 아무리 생각해도, follow 동작이 이상하다.
# 왜 a가 b를 follow했을 때 a가 b의 follower와 following 모두에 등록되지?
@api_view(["POST"])
def user_follow(request):
    login_user = request.user
    target_user = get_object_or_404(
        User, username=request.data["username"], is_active=True
    )
    login_user.following_set.add(target_user)
    target_user.follower_set.add(login_user)
    return Response(status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def user_unfollow(request):
    login_user = request.user
    target_user = get_object_or_404(
        User, username=request.data["username"], is_active=True
    )
    login_user.following_set.remove(target_user)
    target_user.follower_set.remove(login_user)
    return Response(status.HTTP_204_NO_CONTENT)