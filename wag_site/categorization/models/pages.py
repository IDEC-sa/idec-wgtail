from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models

from categorization.models.blocks import Bodycat
from .models import CategoryMp
from wagtail.fields import StreamField, RichTextField
from wagtail_localize.fields import SynchronizedField, TranslatableField



class Category_index_page(Page):
    # unique_id = models.BigAutoField( )
    cat = models.ForeignKey(to=CategoryMp, on_delete=models.CASCADE, related_name="page", unique=False)
    # body = StreamField(brandsContenet(), blank=True)        # new
    bodycat = StreamField(Bodycat(), blank=True)        # new
   
    content_panels = Page.content_panels + [
        FieldPanel('cat'),
        # FieldPanel('body'),
        FieldPanel('bodycat'),

    ]

    def get_context(self, request, *args, **kwargs):
        ctx =  super().get_context(request, *args, **kwargs)
        sub_cats = self.cat.get_descendants()
        subs = []
        for cat in sub_cats:
            if cat.sub_page:
                subs.append(cat.sub_page)
        print(subs)
        if subs:
            ctx["sub_cats"] = subs
        
        return ctx
    # class Meta:
    #     constraints = [
    #     models.UniqueConstraint(fields=['unique_id', 'cat'], name='unique page per cat')
    # ]
        # unique_together = ('cat', 'unique_id')

    override_translatable_fields = [
        TranslatableField("title"),
        SynchronizedField("slug"),
    ]


class SubPage(Page):
    cat = models.ForeignKey(to=CategoryMp, on_delete=models.CASCADE, related_name="sub_page")
    # pass
    content_panels = Page.content_panels + [
        FieldPanel('cat'),
        # FieldPanel('body'),
        # FieldPanel('bodycat')
    ]