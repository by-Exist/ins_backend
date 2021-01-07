from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    # FIXME: 기본적으로 사용되던 validate 로직을 어떻게 포함시켜야 할까?
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "username", "password"]
