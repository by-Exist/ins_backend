from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMAIL = "F", "여성"

    follower_set = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name="팔로워",
    )
    following_set = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name="팔로잉",
    )

    website_url = models.URLField("웹사이트", blank=True)
    bio = models.TextField("sns 정보", blank=True)
    phone_number = models.CharField(
        "전화번호",
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    gender = models.CharField(
        "성별",
        max_length=1,
        blank=True,
        choices=GenderChoices.choices,
    )
    
    avatar = models.ImageField(
        blank=True,
        upload_to="accounts/avatar/%Y/%m/%d"
    )