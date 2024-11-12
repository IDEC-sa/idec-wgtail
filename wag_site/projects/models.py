from django.db import models

# Create your models here.
from wagtail_localize.fields import SynchronizedField, TranslatableField
from wagtail.fields import StreamField, RichTextField

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, PublishingPanel,PageChooserPanel
from wagtail.images.models import Image as WagImage
from wagtail.fields import RichTextField

from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
)
from wagtail.contrib.settings.models import (
    register_setting,
)
from banner.blocks import BodyBlock_banners


# ----------------------------------------------------------------
# ----------------------------------------------------------------


class ProjectIndexPage(Page):
    intro = models.CharField(max_length=255,blank=True)
    sub_title = models.CharField(max_length=255,blank=True)
    title_background = models.CharField(max_length=255,blank=True)
    body = StreamField(BodyBlock_banners(), blank=True)        # new

    subpage_types = ['ProjectDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('sub_title'),
        FieldPanel('title_background'),
        FieldPanel("body"),

    ]



class ProjectDetailPage(Page):
    project_title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField()
    all_description = RichTextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    clients = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    project_year = models.CharField(max_length=4, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    body = StreamField(BodyBlock_banners(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('all_description'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('clients'),
        FieldPanel('area'),
        FieldPanel('location'),
        FieldPanel('project_year'),
        FieldPanel('project_type'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('slider_images', label="Slider images"),
        InlinePanel('slider_images_big', label="Slider images big"),
        FieldPanel("body"),

    ]



class ProjectGalleryImage(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]  


class ProjectSliderImage(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class ProjectSliderImage_big(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='slider_images_big')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]



# ----------------------------------------------------------------


# class IdecHome(Page):

#     body = StreamField(BodyBlock(), blank=True)        

#     content_panels = Page.content_panels + [
#         FieldPanel("body"),
#     ]



