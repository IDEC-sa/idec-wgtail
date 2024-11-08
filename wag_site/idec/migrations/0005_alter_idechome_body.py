# Generated by Django 5.0.6 on 2024-07-03 09:42

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idec', '0004_alter_idechome_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idechome',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('slider', wagtail.blocks.StreamBlock([('slide', wagtail.blocks.StructBlock([('catchy_text', wagtail.blocks.TextBlock()), ('text', wagtail.blocks.TextBlock()), ('dachedText', wagtail.blocks.TextBlock()), ('buttonText', wagtail.blocks.TextBlock()), ('buttonUrl', wagtail.blocks.URLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))])), ('about', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('main_info', wagtail.blocks.StreamBlock([('main_info_member', wagtail.blocks.StructBlock([('main_text', wagtail.blocks.TextBlock()), ('description', wagtail.blocks.TextBlock())]))])), ('intro_with_background', wagtail.blocks.StructBlock([('background_text', wagtail.blocks.TextBlock()), ('main_text', wagtail.blocks.TextBlock()), ('brief', wagtail.blocks.TextBlock())]))])), ('projects', wagtail.blocks.StreamBlock([('project', wagtail.blocks.PageChooserBlock(page_type=['idec.ProjectDetailPage'], required=True))])), ('feedback', wagtail.blocks.StreamBlock([('feedback', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('rate', wagtail.blocks.CharBlock(max_length=200, required=False)), ('icon', wagtail.blocks.CharBlock(max_length=200, required=False))]))])), ('aboutvideo', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('subtitle', wagtail.blocks.CharBlock(max_length=200, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.CharBlock(max_length=200, required=False)), ('button', wagtail.blocks.CharBlock(max_length=200, required=False))])), ('services', wagtail.blocks.StreamBlock([('service', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('sub_title', wagtail.blocks.CharBlock(max_length=200, required=False))]))])), ('gallery', wagtail.blocks.StreamBlock([('category', wagtail.blocks.PageChooserBlock(page_type=['idec.CategoryPage'], required=True))]))], blank=True),
        ),
    ]
