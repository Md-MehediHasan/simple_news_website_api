# Generated by Django 5.0.2 on 2024-02-20 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_news_read_times_alter_news_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='advertisement')),
                ('position', models.CharField(choices=[('Insection_ad', 'InSection_ad'), ('top', 'Top'), ('sidebar', 'Sidebar')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 9, 38, 0, 695949, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
