# Generated by Django 2.2 on 2019-04-06 08:29

import api_auth.models.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='createdAt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedAt')),
                ('key', models.CharField(default=api_auth.models.utils.generateApiKey, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
