from django.db import models

# Create your models here.

from wagtail.fields import StreamField, RichTextField
from .blocks import BodyBlock, HomeAboutBlock,Projects
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel





class ProjectIndexPage(Page):
    intro = RichTextField(blank=True)

    subpage_types = ['ProjectDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]



class ProjectDetailPage(Page):
    project_title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    clients = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    project_year = models.CharField(max_length=4, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)





    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('clients'),
        FieldPanel('area'),
        FieldPanel('project_year'),
        FieldPanel('project_type'),
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