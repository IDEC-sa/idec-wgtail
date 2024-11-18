from django.db import models

# Create your models here.

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from wagtail.snippets.models import register_snippet
from wagtail.models import AbstractPage, ClusterableModel
# from wagtail.models import PageBase
from wagtail.admin.panels import FieldPanel
from wagtailmetadata.models import MetadataPageMixin
# from .pages import Category_index_page
# from wagtail.models import Page
# class Categoryy_index_page(Page):
#     pass
from categorization.models.models import CategoryMp

@register_snippet
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.OneToOneField(CategoryMp, on_delete=models.DO_NOTHING, related_name="prod_page")
    
    panels = [
        FieldPanel("name"),
    ]

    # def __str__(self):
    #     # print()
    #     return " >  ".join([a.name for a in self.get_ancestors(include_self=True)])
