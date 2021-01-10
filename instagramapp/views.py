from datetime import timedelta
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = (
        Post.objects.all()
        .select_related("author")
        .prefetch_related("tag_set", "like_user_set")
    )
    serializer_class = PostSerializer
    # permission_classes = [AllowAny]  # FIXME: 인증 적용

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(["POST"], True)
    def like(self, request, pk):
        post = self.get_object()
        post.like_user_set.add(request.user)
        return Response(status.HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self, request, pk):
        post = self.get_object()
        post.like_user_set.remove(request.user)
        return Response(status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        timesince = timezone.now() - timedelta(days=3)
        qs = super().get_queryset()
        qs = qs.filter(
            Q(author=self.request.user)
            | Q(author__in=self.request.user.following_set.all())
        )
        qs = qs.filter(created_at__gte=timesince)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__pk=self.kwargs["post_pk"])
        return qs

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        serializer.save(author=self.request.user, post=post)
        return super().perform_create(serializer)