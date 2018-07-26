from django.conf import settings
from django.db import models


class Quest(models.Model):
    name = models.CharField(max_length=255)
    # XXX: we need our own quest markup?
    description = models.TextField()
    should_after = models.ManyToManyField('self')
    minimum_should_after = models.IntegerField()
    must_after = models.ManyToManyField('self')


class UserQuest(models.Model):

    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    surfer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issued_quests', on_delete=models.CASCADE)
    confirmed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='confirmed_quests', on_delete=models.CASCADE)

    date_opened = models.DateTimeField()
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()

    class State:
        NEW = 'NEW'
        DECLINED = 'DECLINED'
        OUTDATED = 'OUTDATED'
        OPENED = 'OPENED'
        STARTED = 'STARTED'
        FINISHED = 'FINISHED'

    state = models.CharField(max_length=255, choices=[
        (State.NEW, 'New quest'),
        (State.DECLINED, 'Declined'),
        (State.OUTDATED, 'Outdated'),
        (State.OPENED, 'User has seen this quest'),
        (State.STARTED, 'User accepted the quest'),
        (State.FINISHED, 'Finished'),
    ])


class QuestMedia(models.Model):

    surfer_quest = models.ForeignKey(UserQuest, on_delete=models.CASCADE)

    class MediaType:
        PHOTO = 'PHOTO'
        VIDEO = 'VIDEO'
        SOUND = 'SOUND'
        TEXT = 'TEXT'
        URL = 'URL'

    media_type = models.CharField(max_length=255, choices=[
        (MediaType.PHOTO, 'Photo'),
        (MediaType.VIDEO, 'Video'),
        (MediaType.SOUND, 'Sound'),
        (MediaType.TEXT, 'Text'),
        (MediaType.URL, 'Url'),
    ])

    description = models.CharField(max_length=255)
