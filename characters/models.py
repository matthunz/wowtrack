from django.contrib.auth.models import User
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=12)
    realm = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('name', 'realm')

    def __str__(self):
        return '%s - %s' % (self.name, self.realm)


class Snapshot(models.Model):
    character = models.ForeignKey(Character)
    item_level = models.IntegerField()
