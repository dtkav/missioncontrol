# Generated by Django 2.1.4 on 2019-01-16 06:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import home.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_cached_access_bucket_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('environment', models.CharField(blank=True, max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('tasks', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('created', home.models.ISODateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='pass',
            name='task_stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='home.TaskStack', to_field='uuid'),
        ),
        migrations.AddField(
            model_name='satellite',
            name='task_stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='home.TaskStack', to_field='uuid'),
        ),
    ]