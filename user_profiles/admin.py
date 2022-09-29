from django.contrib import admin

from . import models
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)