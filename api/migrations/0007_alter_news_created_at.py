# Generated by Django 5.0.2 on 2024-02-16 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 16, 51, 44, 153918, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
