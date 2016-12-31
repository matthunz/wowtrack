from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
import requests


class Character(models.Model):
    name = models.CharField(max_length=12)
    realm = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('name', 'realm')

    def clean(self):
        request = requests.get(
            'https://us.api.battle.net/wow/character/%s/%s?locale=en_US&fields=items&apikey=%s' % (
                self.realm, self.name, 'x95frpjm3v3zdrnj3rbzr83e9b348hj9'
            ))

        if request.status_code != 200:
            raise ValidationError('Character not found')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Character, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.name, self.realm)


class Snapshot(models.Model):
    character = models.ForeignKey(Character)
    item_level = models.IntegerField()
