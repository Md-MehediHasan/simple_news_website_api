# Generated by Django 5.0.2 on 2024-02-17 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_news_created_at_alter_newsphoto_news_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 17, 4, 3, 8, 51292, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
