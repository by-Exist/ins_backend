from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    # FIXME: 기본적으로 사용되던 validate 로직을 어떻게 포함시켜야 할까?
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        nickname = validated_data["nickname"]
        user = User.objects.create(username=username, nickname=nickname)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "username", "password", "nickname"]


class SuggestionUserSerializer(serializers.ModelSerializer):

    already_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "nickname", "avatar", "already_following"]

    def get_already_following(self, user):
        # 반드시 로그인되어있는 상황이라고 가정
        login_user = self.context.get("request").user
        get_already_following = login_user.following_set.filter(
            username=user.username
        ).exists()
        return get_already_following