from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models
from .models import CategoryMp



class Category_index_page(Page):
    cat = models.OneToOneField(to=CategoryMp, on_delete=models.CASCADE)

    content_panels = Page.content_panels + [
        FieldPanel('cat'),
    ]