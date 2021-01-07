import re
from django.conf import settings
from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자"
    )
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like_post_set"
    )
    tag_set = models.ManyToManyField("Tag", blank=True)

    caption = models.CharField("캡션", max_length=500)
    photo = models.ImageField("사진", upload_to="instagram/post/%Y/%m/%d")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#[a-zA-Z\dㄱ-힣]+", self.caption)
        tag_list = [
            Tag.objects.get_or_create(name=tag_name) for tag_name in tag_name_list
        ]
        return tag_list

    def get_absolute_url(self):
        return reverse("instagramapp:post_detail", args=[self.pk])

    def is_like_user(self, user):
        return self.like_user_set.filter(pk=user.pk).exists()

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="포스트",
    )
    message = models.TextField("댓글내용")


class Tag(TimeStampedModel):
    name = models.CharField("태그", max_length=20, unique=True)

    def __str__(self):
        return self.name