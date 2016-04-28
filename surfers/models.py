from django.contrib.gis.db import models
from django.conf import settings


class LatestPoint(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    updated_at = models.DateTimeField(auto_now=True)
    point = models.PointField(geography=True)

    class Meta:
        verbose_name_plural = 'Latest Point'


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    contact_type = models.CharField(max_length=32, choices=[

        # XXX: или показывать по-дефолту из auth.User?
        # против - пользователь должен явно указать публичный e-mail,
        # auth.User.email - не публичный
        ('EMAIL', 'Email'),

        # XXX: нужен тут дефолтный или пусть в UserLocation?
        # ('PHONE', 'Phone'),

        ('FB', 'Facebook'),
        ('VK', 'ВКонтакте'),
        ('IG', 'Instagram'),
        ('TW', 'Twitter'),

        # XXX: всё это обычно один номер телефона, но наверно лучше дать явно
        # указать
        ('TELEGRAM', 'Telegram'),
        ('WHATSUP', 'WhatsUp'),
        ('VIBER', 'Viber'),

        ('OTHER', 'Other'),
    ])
    value = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)


class Achievment(models.Model):
    name = models.CharField(max_length=255)
    base_score = models.IntegerField()


class UserAchievment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    achievment = models.ForeignKey(Achievment)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Endorsement(models.Model):
    achievment = models.ForeignKey(UserAchievment)
    endorsed_by = models.ForeignKey(settings.AUTH_USER_MODEL)


class Location(models.Model):
    name = models.CharField(max_length=255)
    geo = models.GeometryField()


class UserLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    location = models.ForeignKey(Location)
    date_from = models.DateTimeField()
    date_till = models.DateTimeField()
    contact_phone = models.CharField(max_length=32)


class Track(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    point = models.PointField()
    timestamp = models.DateTimeField(auto_now_add=True)
