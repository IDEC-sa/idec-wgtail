from django.db import models

# Create your models here.

from wagtail.fields import StreamField, RichTextField
from .blocks import BodyBlock, HomeAboutBlock,Projects

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
from .blocks import BodyBlock, HomeAboutBlock, BranchBlock, GalleryBlock
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




class ProjectIndexPage(Page):
    intro = models.CharField(max_length=255,blank=True)
    sub_title = models.CharField(max_length=255,blank=True)

    subpage_types = ['ProjectDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('sub_title')

    ]



class ProjectDetailPage(Page):
    project_title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField()
    all_description = RichTextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    clients = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    project_year = models.CharField(max_length=4, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('all_description'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('clients'),
        FieldPanel('area'),
        FieldPanel('location'),
        FieldPanel('project_year'),
        FieldPanel('project_type'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('slider_images', label="Slider images"),
        InlinePanel('slider_images_big', label="Slider images big"),
    ]



class ProjectGalleryImage(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]  


class ProjectSliderImage(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class ProjectSliderImage_big(Orderable):
    page = ParentalKey(ProjectDetailPage, on_delete=models.CASCADE, related_name='slider_images_big')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class IdecHome(Page):
    # header_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name="+",
    # )

    body = StreamField(BodyBlock(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel("body"),
                       # new
    ]

class Branch(Page):
    city = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    content_panels = Page.content_panels + [
                       # new
                       FieldPanel("city"),
                       FieldPanel("address"),
                       FieldPanel("phone"),
                       FieldPanel("email"),
    ]

@register_setting
class NavigationSettings(BaseGenericSetting):
    company_name  = models.TextField(blank=False, default="IDEC")
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    fb_url = models.URLField(verbose_name="Facebook URL", blank=True)
    linkedin_url = models.URLField(verbose_name="Linkedin URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)

    content_panels = Page.content_panels + [
                       # new
    ]
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("instagram_url"),
                FieldPanel("twitter_url"),
                FieldPanel("fb_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("company_name"),
            ],
            "Social settings",
        )
    ]

# ...keep the definition of the NavigationSettings model and add the FooterText model:
@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "idec/idec_home.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"

class CategoryPage(Page):
    image = WagtailImageField()
    name  = models.TextField()
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('description')
    ]

# class Branch(Page):
#     city = models.TextField()
#     address = models.TextField()
#     phone = models.TextField()
#     email = models.TextField()
#     content_panels = Page.content_panels + [
#                        # new
#                        FieldPanel("city"),
#                        FieldPanel("address"),
#                        FieldPanel("phone"),
#                        FieldPanel("email"),
#     ]

# @register_setting
# class NavigationSettings(BaseGenericSetting):
#     company_name  = models.TextField(blank=False, default="IDEC")
#     twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
#     fb_url = models.URLField(verbose_name="Facebook URL", blank=True)
#     linkedin_url = models.URLField(verbose_name="Linkedin URL", blank=True)
#     github_url = models.URLField(verbose_name="GitHub URL", blank=True)
#     instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)

#     content_panels = Page.content_panels + [
#                        # new
#     ]
#     panels = [
#         MultiFieldPanel(
#             [
#                 FieldPanel("twitter_url"),
#                 FieldPanel("github_url"),
#                 FieldPanel("instagram_url"),
#                 FieldPanel("twitter_url"),
#                 FieldPanel("fb_url"),
#                 FieldPanel("linkedin_url"),
#                 FieldPanel("company_name"),
#             ],
#             "Social settings",
#         )
#     ]

# ...keep the definition of the NavigationSettings model and add the FooterText model:
# @register_snippet
# class FooterText(
#     DraftStateMixin,
#     RevisionMixin,
#     PreviewableMixin,
#     TranslatableMixin,
#     models.Model,
# ):

#     body = RichTextField()

#     panels = [
#         FieldPanel("body"),
#         PublishingPanel(),
#     ]

#     def __str__(self):
#         return "Footer text"

#     def get_preview_template(self, request, mode_name):
#         return "idec/idec_home.html"

#     def get_preview_context(self, request, mode_name):
#         return {"footer_text": self.body}

#     class Meta(TranslatableMixin.Meta):
#         verbose_name_plural = "Footer Text"



# class Projects(Page):

#     body = StreamField(Projects(), blank=True)    

#     content_panels = Page.content_panels + [
#         FieldPanel("body"),
                     
#     ]