# Generated by Django 5.0.2 on 2024-03-16 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_advertisement_url_alter_news_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 13, 48, 10, 88667, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
