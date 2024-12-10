from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.core.exceptions import ValidationError

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



def validate_category_level(value):
    category = CategoryMp.objects.get(id=value)
    if not category.parent:
        raise ValidationError("The category should has a parent category.")

@register_snippet
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    internalCode = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(CategoryMp, on_delete=models.DO_NOTHING, related_name="product", validators=[validate_category_level])
    brand = models.ForeignKey("brands.Brand", on_delete=models.DO_NOTHING, related_name="product")
    panels = [
        FieldPanel("name"),
        FieldPanel('category'),
        FieldPanel("brand")
    ]
    def __str__(self):
        # print()
        return self.name


