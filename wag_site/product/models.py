from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
# from .blocks import BodyBlock, HomeAboutBlock, BranchBlock, GalleryBlock
from wagtail.admin.panels import FieldPanel, InlinePanel, PublishingPanel
from wagtail.images.models import Image as WagImage
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet

# add this:
from wagtail.search import index

from wagtail.fields import StreamField, RichTextField

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, PublishingPanel
from wagtail.images.models import Image as WagImage
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from brands.models import BrandsDetailPage  # تأكد من استيراد الموديل بشكل صحيح
# from idec.models import CategoryPage  # تأكد من استيراد الموديل بشكل صحيح

class productIndexPage(Page):

    product_intro = models.CharField(max_length=255, blank=True)
    product_sub_title = models.CharField(max_length=255, blank=True)
    product_background = models.CharField(max_length=255, blank=True)

    subpage_types = ['productDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('product_intro'),
        FieldPanel('product_sub_title'),
        FieldPanel('product_background'),

    ]

class productDetailPage(Page):
    product_title = models.CharField(max_length=255)
    product_subtitle = models.CharField(max_length=255, blank=True, null=True)
    product_description = RichTextField()
    product_details = RichTextField()
    # blog_start_date = models.DateTimeField()  # تأكد من أن الحقل موجود في النموذج
    product_type = models.CharField(max_length=255)
    brand = models.ForeignKey('brands.BrandsDetailPage', on_delete=models.SET_NULL, null=True, blank=True, related_name='brand')
    category = models.ForeignKey('idec.CategoryPage', on_delete=models.SET_NULL, null=True, blank=True)
    # subCategoryPage = models.ForeignKey('idec.SubCategoryPage', on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('product_title'),
        FieldPanel('product_subtitle'),
        FieldPanel('product_description'),
        FieldPanel('product_details'),
        FieldPanel('brand'),
        FieldPanel('category'),
        # FieldPanel('subCategoryPage'),

        # FieldPanel('blog_start_date'),
        FieldPanel('product_type'),
        InlinePanel('gallery_images_product', label="Gallery images"),
        InlinePanel('gallery_images_product_bg', label="Gallery images bg"),

    ]

class productGalleryImage(Orderable):
    page = ParentalKey(productDetailPage, on_delete=models.CASCADE, related_name='gallery_images_product')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class productliGalleryImage(Orderable):
    page = ParentalKey(productDetailPage, on_delete=models.CASCADE, related_name='gallery_images_product_bg')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]