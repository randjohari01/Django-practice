from django.contrib import admin
from . import models
from .models import Runner #just to reminder there is another way to do that

admin.site.register(models.article)

admin.site.register(models.personshirt)
admin.site.register(Runner)
admin.site.register(models.Fruit)