from django.db import models

# Create your models here.

from wagtail.fields import StreamField, RichTextField
from .blocks import  BodyBlock_about

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.models import WagtailImageField
from wagtail.fields import StreamField
from .blocks import BodyBlock_about, HomeAboutBlock, BranchBlock
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


class aboutHome(Page):


    body = StreamField(BodyBlock_about(), blank=True)        # new

    content_panels = Page.content_panels + [
        FieldPanel("body"),
                       # new
    ]
