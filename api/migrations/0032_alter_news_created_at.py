# Generated by Django 5.0.2 on 2024-04-09 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 9, 22, 59, 34, 763997, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
