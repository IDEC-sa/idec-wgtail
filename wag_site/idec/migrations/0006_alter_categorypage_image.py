# Generated by Django 5.0.6 on 2024-07-03 09:58

import wagtail.images.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idec', '0005_alter_idechome_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypage',
            name='image',
            field=wagtail.images.models.WagtailImageField(upload_to=''),
        ),
    ]