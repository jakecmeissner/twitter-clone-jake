# Generated by Django 4.1.1 on 2022-09-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name'),
        ),
    ]