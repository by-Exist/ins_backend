from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "nickname", "avatar"]


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    is_like_user = serializers.SerializerMethodField("is_like_field")

    def is_like_field(self, post):
        if hasattr(self.context["request"], "user"):
            user = self.context["request"].user
            return post.like_user_set.filter(pk=user.pk).exists()
        else:
            return False

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "created_at",
            "photo",
            "caption",
            "location",
            "tag_set",
            "is_like_user",
        ]


class CommentSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "created_at", "updated_at", "message"]