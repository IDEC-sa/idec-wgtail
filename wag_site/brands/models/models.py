from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel


@register_snippet
class Brand(models.Model):
    name=models.CharField(max_length=50, unique=True)
    # brand_page = models.ForeignKey("brands.BrandsDetailPage", on_delete=models.DO_NOTHING, related_name="brand")


    def __str__(self):
        return self.name
