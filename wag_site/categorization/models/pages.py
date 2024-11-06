from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models

from categorization.models.blocks import Bodycat
from .models import CategoryMp
from wagtail.fields import StreamField, RichTextField



class Category_index_page(Page):
    cat = models.OneToOneField(to=CategoryMp, on_delete=models.CASCADE)
    # body = StreamField(brandsContenet(), blank=True)        # new
    bodycat = StreamField(Bodycat(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel('cat'),
        # FieldPanel('body'),
        FieldPanel('bodycat'),

    ]