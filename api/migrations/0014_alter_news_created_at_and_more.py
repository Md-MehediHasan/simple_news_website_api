# Generated by Django 5.0.2 on 2024-02-17 06:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_headers_alter_news_created_at_subheaders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 17, 6, 50, 33, 936871, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='subheaders',
            name='referece_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subheaders_ref', to='api.headers'),
        ),
    ]
