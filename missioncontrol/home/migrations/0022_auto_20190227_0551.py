# Generated by Django 2.1.4 on 2019-02-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_s3files_20190227_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s3file',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='s3file',
            name='what',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s3file',
            name='where',
            field=models.TextField(),
        ),
    ]