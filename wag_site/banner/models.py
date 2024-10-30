from django.db import models

# Create your models here.

from wagtail.fields import StreamField, RichTextField
# from .blocks import   BodyBlock_banner

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
# from .blocks import BodyBlock_about, HomeAboutBlock, BranchBlock
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












# --------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# --------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------










# ------------------------------------------------------------------

# نموذج الصفحة الرئيسية لعرض البانر
class BannerIndexPage(Page):
    banner_intro = models.CharField(max_length=255, blank=True)
    banner_sub_title = models.CharField(max_length=255, blank=True)
    banner_title_background = models.CharField(max_length=255, blank=True)
    subpage_types = ['BannerDetailPage']  # تأكد من استخدام الأسماء الصحيحة للنماذج الفرعية

    content_panels = Page.content_panels + [
        FieldPanel('banner_intro'),
        FieldPanel('banner_sub_title'),
        FieldPanel('banner_title_background'),
    ]

# نموذج الصفحة التفصيلية للبانر
class BannerDetailPage(Page):
    title_banner = models.CharField(max_length=255)
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True)
    link_banner = RichTextField()
    button_banner = models.CharField(max_length=255)  # تأكد من أن هذا هو النص المناسب للرابط

    content_panels = Page.content_panels + [
        FieldPanel('title_banner'),
        FieldPanel('subtitle_banner'),
        FieldPanel('link_banner'),
        FieldPanel('button_banner'),  # يمكنك تغييره حسب الحاجة
        InlinePanel('gallery_images', label="Gallery images"),  # تأكد من أن الاسم صحيح
    ]

# نموذج لصور المعرض
class BannerIndexGalleryImage(Orderable):
    page = ParentalKey(BannerDetailPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
