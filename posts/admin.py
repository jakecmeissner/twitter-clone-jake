from django.contrib import admin

from . import models
from .models import Post

# Register your models here.
admin.site.register(Post)