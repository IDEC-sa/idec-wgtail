from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
            FieldPanel('body'),
        ]
    
from wagtail.fields import StreamField
from .blocks import BodyBlock


class PostPage(Page):
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # tags = ClusterTaggableManager(through="blog.PostPageTag", blank=True)

    body = StreamField(BodyBlock(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        # InlinePanel("categories", label="category"),
        # FieldPanel("tags"),
        FieldPanel("body"),                           # new
    ]
