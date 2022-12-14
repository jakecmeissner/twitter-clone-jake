from email.policy import default
from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous', 
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True 
    )
    createdAt = models.DateTimeField(
        'Created DateTime', blank=True,  auto_now_add=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True, 
    )
    like = models.PositiveIntegerField(
        'like', default=0, blank=True, db_index=True
    )
