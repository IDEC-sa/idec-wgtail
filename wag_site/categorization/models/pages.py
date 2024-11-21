from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models
from django.db.models import Q

from categorization.models.blocks import Bodycat
from .models import CategoryMp
from wagtail.fields import StreamField, RichTextField
from wagtail_localize.fields import SynchronizedField, TranslatableField
from product import models as prod_models
# from product.models.pages import productDetailPage
from brands import models as brand_models

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
        products = prod_models.models.Product.objects.filter(category__in=sub_cats).values("id").distinct()
        brands = []
        brands = prod_models.models.Product.objects.filter(category__in=sub_cats).values("brand").distinct()
        brand_pages =  brand_models.pages.BrandsDetailPage.objects.filter(brand__in = brands)
        sub_cat_pages = SubPage.objects.filter(cat__in=sub_cats)
        product_pages = prod_models.pages.productDetailPage.objects.filter(product__in=products)[:10]
        print("products")
        print(product_pages)
        if brand_pages:
            ctx["brand_pages"] = brand_pages
        if sub_cat_pages:
            ctx['sub_cat_pages'] = sub_cat_pages
        if product_pages:
            ctx["product_pages"] = product_pages
        return ctx

    override_translatable_fields = [
        TranslatableField("title"),
        SynchronizedField("slug"),
    ]


class SubPage(Page):
    cat = models.ForeignKey(to=CategoryMp, on_delete=models.CASCADE, related_name="sub_page")
    # pass
    image_logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('cat'),
        FieldPanel('image_logo')
    ]

    def get_context(self, request, *args, **kwargs):
        ctx =  super().get_context(request, *args, **kwargs)
        parent = self.cat.parent
        siblings = parent.get_descendants(include_self=True)
        products = prod_models.models.Product.objects.filter(Q(category=self.cat)).values("id").distinct()
        brands = prod_models.models.Product.objects.filter(Q(category=self.cat)).values("brand").distinct()
        brand_pages = brand_models.pages.BrandsDetailPage.objects.filter(Q(brand__in=brands))
        product_pages = prod_models.pages.productDetailPage.objects.filter(Q(product__in=products))
        ctx["cats"] = siblings
        if brand_pages:
            ctx['brand_pages'] = brand_pages
        if product_pages:
            ctx["product_pages"] = product_pages
        return ctx
