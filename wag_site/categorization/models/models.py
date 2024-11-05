from django.db import models

# Create your models here.

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from wagtail.snippets.models import register_snippet
from wagtail.models import AbstractPage, ClusterableModel
# from wagtail.models import PageBase
from wagtail.admin.panels import FieldPanel
from wagtailmetadata.models import MetadataPageMixin

from wagtail.models import Page
class Categoryy_index_page(Page):
    pass


@register_snippet
class CategoryMp(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # class MPTTMeta:
    #     order_insertion_by = ['name']
    
    panels = [
        FieldPanel("name"),
        FieldPanel("parent"),
    ]

    def __str__(self):
        # print()
        return " >  ".join([a.name for a in self.get_ancestors(include_self=True)])
