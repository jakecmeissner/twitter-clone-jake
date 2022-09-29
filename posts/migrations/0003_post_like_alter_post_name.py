# Generated by Django 4.1.1 on 2022-09-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=20, verbose_name='Name'),
        ),
    ]
