# Generated by Django 5.0.2 on 2024-04-09 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 9, 13, 22, 8, 132988, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
