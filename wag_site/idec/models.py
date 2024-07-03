from django.db import models

# Create your models here.

from wagtail.fields import StreamField
from .blocks import BodyBlock, HomeAboutBlock, BranchBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel, PublishingPanel

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
