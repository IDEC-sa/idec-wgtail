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

class BrandsIndexPage(Page):

    Brands_intro = models.CharField(max_length=255, blank=True)
    Brands_sub_title = models.CharField(max_length=255, blank=True)
    Brands_background = models.CharField(max_length=255, blank=True)

    subpage_types = ['BrandsDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('Brands_intro'),
        FieldPanel('Brands_sub_title'),
        FieldPanel('Brands_background'),

    ]

class BrandsDetailPage(Page):
    Brands_title = models.CharField(max_length=255)
    Brands_subtitle = models.CharField(max_length=255, blank=True, null=True)
    Brands_description = RichTextField()
    # blog_start_date = models.DateTimeField()  # تأكد من أن الحقل موجود في النموذج
    Brands_type = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('Brands_title'),
        FieldPanel('Brands_subtitle'),
        FieldPanel('Brands_description'),
        # FieldPanel('blog_start_date'),
        FieldPanel('Brands_type'),
        InlinePanel('gallery_images_Brands', label="Gallery images"),
    ]

class BrandsGalleryImage(Orderable):
    page = ParentalKey(BrandsDetailPage, on_delete=models.CASCADE, related_name='gallery_images_Brands')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

