from django.contrib import admin

from . import models
from .models import Post
from .models import Picture

# Register your models here.
admin.site.register(Post)
admin.site.register(Picture)