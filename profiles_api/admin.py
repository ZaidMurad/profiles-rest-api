from django.contrib import admin
from . import models

# Register your models here with the admin site.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
