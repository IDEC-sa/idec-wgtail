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
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel

from banner.blocks import BodyBlock_banners

class BlogIndexPage(Page):

    blog_intro = models.CharField(max_length=255, blank=True)
    blog_sub_title = models.CharField(max_length=255, blank=True)
    blog_background = models.CharField(max_length=255, blank=True)
    body = StreamField(BodyBlock_banners(), blank=True)        # new

    subpage_types = ['BlogDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('blog_intro'),
        FieldPanel('blog_sub_title'),
        FieldPanel('blog_background'),
        FieldPanel("body"),

    ]

class BlogDetailPage(Page):
    blog_title = models.CharField(max_length=255)
    blog_subtitle = models.CharField(max_length=255, blank=True, null=True)
    blog_description = RichTextField()
    # blog_start_date = models.DateTimeField()  # تأكد من أن الحقل موجود في النموذج
    # blog_type = models.CharField(max_length=255)
    blog_date = models.DateTimeField("Publication Date", blank=True, null=True)  # أضف حقل التاريخ هنا
    category = models.ForeignKey(  # تغيير الاسم إلى 'category'
        'idec.CategoryPage', 
        null=True,  # السماح بقيمة null
        blank=True,  # السماح بترك الحقل فارغًا
        on_delete=models.SET_NULL,  # تعيينه إلى null إذا تم حذف الصفحة المرتبطة
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_subtitle'),
        FieldPanel('blog_description'),
        # FieldPanel('blog_start_date'),
        # FieldPanel('blog_type'),
        InlinePanel('gallery_images_blog', label="Gallery images"),
        FieldPanel('blog_date'),  # إضافة حقل التاريخ إلى اللوحة
        PageChooserPanel('category', 'idec.CategoryPage'),  # تغيير هنا إلى 'category'

    ]

class BlogGalleryImage(Orderable):
    page = ParentalKey(BlogDetailPage, on_delete=models.CASCADE, related_name='gallery_images_blog')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
