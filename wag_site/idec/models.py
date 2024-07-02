from django.db import models

# Create your models here.

from wagtail.fields import StreamField, RichTextField
from .blocks import BodyBlock, HomeAboutBlock,Projects

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey




class ProjectIndexPage(Page):
    intro = models.CharField(max_length=255,blank=True)
    sub_title = models.CharField(max_length=255,blank=True)

    subpage_types = ['ProjectDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('sub_title')

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




class IdecHome(Page):
    # header_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name="+",
    # )

    body = StreamField(BodyBlock(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel("body"),
                       # new
    ]



# class Projects(Page):

#     body = StreamField(Projects(), blank=True)    

#     content_panels = Page.content_panels + [
#         FieldPanel("body"),
                     
#     ]