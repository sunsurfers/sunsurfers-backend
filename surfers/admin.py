from django.contrib.gis import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from surfers import models


admin.site.register(models.Achievment)
admin.site.register(models.Location)


class LatestPointInline(admin.StackedInline):
    model = models.LatestPoint


class ContactInline(admin.TabularInline):
    model = models.Contact


admin.site.unregister(get_user_model())


GisUserAdmin = type('GisUserAdmin', (UserAdmin, admin.GeoModelAdmin,),
                    dict(UserAdmin.__dict__))


class SurferAdmin(GisUserAdmin):
    inlines = UserAdmin.inlines + [
        LatestPointInline,
        ContactInline,
    ]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide inlines in the add view
            if obj is None:
                continue
            yield inline.get_formset(request, obj), inline


admin.site.register(get_user_model(), SurferAdmin)
