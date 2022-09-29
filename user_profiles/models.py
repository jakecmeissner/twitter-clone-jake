from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    class Meta(object):
        db_table = 'user_profile'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous', 
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'