from django.contrib import admin
from . import models


class SnapshotInline(admin.StackedInline):
    model = models.Snapshot


class CharacterAdmin(admin.ModelAdmin):
    inlines = [SnapshotInline]


admin.site.register(models.Character, CharacterAdmin)
