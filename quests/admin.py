from django.contrib.gis import admin

from quests.models import Quest, UserQuest

admin.site.register(Quest)
admin.site.register(UserQuest)
