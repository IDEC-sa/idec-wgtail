# Generated by Django 5.0.6 on 2024-07-01 11:51

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idec', '0016_rename_mastodon_url_navigationsettings_instagram_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idechome',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('slider', wagtail.blocks.StreamBlock([('slide', wagtail.blocks.StructBlock([('catchy_text', wagtail.blocks.TextBlock()), ('text', wagtail.blocks.TextBlock()), ('dachedText', wagtail.blocks.TextBlock()), ('buttonText', wagtail.blocks.TextBlock()), ('buttonUrl', wagtail.blocks.URLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))])), ('about', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('main_info', wagtail.blocks.StreamBlock([('main_info_member', wagtail.blocks.StructBlock([('main_text', wagtail.blocks.TextBlock()), ('description', wagtail.blocks.TextBlock())]))])), ('intro_with_background', wagtail.blocks.StructBlock([('background_text', wagtail.blocks.TextBlock()), ('main_text', wagtail.blocks.TextBlock()), ('brief', wagtail.blocks.TextBlock())]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='navigationsettings',
            name='instagram_url',
            field=models.URLField(blank=True, verbose_name='Instagram URL'),
        ),
    ]
