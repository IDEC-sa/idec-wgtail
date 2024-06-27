from django.db import models

# Create your models here.

from wagtail.fields import StreamField
from .blocks import BodyBlock, HomeAboutBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel


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
