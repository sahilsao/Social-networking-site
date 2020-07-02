# Generated by Django 3.0.6 on 2020-07-01 17:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_remove_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(blank=True, null=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
