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


from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.models import Image as WagImage
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import RichTextField, StreamField

































@register_snippet
class Product_Requst_form(models.Model):

    # معلومات المنتج
    # product_name = models.CharField(max_length=255, verbose_name="Product Name")

    # البيانات الشخصية
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")

    # الرسالة
    message = models.TextField(verbose_name="Message", blank=True, null=True)

    # الموافقة على سياسة الخصوصية
    agree_to_policy = models.BooleanField(default=False, verbose_name="Agree to Privacy Policy")

    # بيانات التوقيت
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Request by {self.first_name} {self.last_name}"
















def validate_category_level(value):
    category = CategoryMp.objects.get(id=value)
    if not category.parent:
        raise ValidationError("The category should has a parent category.")

@register_snippet
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
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





