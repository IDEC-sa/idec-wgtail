from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.db import models
from django.db.models import Q

from .blocks import Bodycat, intro_with_background
from .models import CategoryMp
from wagtail.fields import StreamField, RichTextField
from wagtail_localize.fields import SynchronizedField, TranslatableField
from product import models as prod_models
# from product.models.pages import productDetailPage
from brands import models as brand_models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path


class Category_index_page( Page):
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
        brand_pages =  brand_models.pages.brand_landing.objects.filter(brand__in = brands)
        sub_cat_pages = SubPage.objects.filter(cat__in=sub_cats)
        product_pages = prod_models.pages.productDetailPage.objects.filter(product__in=products)
        print("products")
        print(product_pages)
        if brand_pages:
            ctx["brand_pages"] = brand_pages
        if sub_cat_pages:
            ctx['sub_cat_pages'] = sub_cat_pages
        if product_pages:
            ctx["product_pages"] = product_pages
        # ctx['posts'] = self.get_paginated_posts(request, self.posts)
        return ctx

    override_translatable_fields = [
    TranslatableField("title"),
    SynchronizedField("slug"),
    ]


class SubPage(RoutablePageMixin, Page):
    cat = models.ForeignKey(to=CategoryMp, on_delete=models.CASCADE, related_name="sub_page")
    # pass
    header_sec = StreamField([("intro_with_background", intro_with_background())], max_num=1, min_num=1)
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
        brand_pages = brand_models.pages.brand_landing.objects.filter(Q(brand__in=brands))
        product_pages = self.get_paginated_prods( self.get_prods())
        ctx["cats"] = siblings
        if brand_pages:
            ctx['brand_pages'] = brand_pages
        if product_pages:
            ctx["product_pages"] = product_pages
        return ctx

    def get_prods(self, additional_filters={}):
        
        products = prod_models.models.Product.objects.filter(Q(category=self.cat))
        print(additional_filters)
        if additional_filters.get('brand', None):
            print(additional_filters['brand'])
            print("lol")
            products = products.filter(Q(brand__name=additional_filters['brand']))
        products = products.values("id").distinct()
        print(products)
        return prod_models.pages.productDetailPage.objects.filter(product__in=products)

    def get_paginated_prods(self, qs, page=None):
        paginator = Paginator(qs, 3)
        # page = 1

        try:
            posts = paginator.page(page)
            print(posts.number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.object_list.none()
        return posts
    

    @re_path(r'^products/$', name="products")
    def next_page(self, request,):
        # brand = request.Grequest.GET.get('brand', None)
        # print(brand)
        additional_filters = {}
        brand = request.GET.get('brand', None)
        print(f"brand{brand}")
        if brand:
            print(additional_filters)
            additional_filters['brand'] = brand
            
        return self.render(
            request,
            context_overrides={"query":{"brand":brand if brand else None},
                'product_pages': self.get_paginated_prods(self.get_prods(additional_filters=additional_filters), request.GET.get('pages', 1)
) ,
            },
            template="categorization/paginated_cat_prods.html",
        )

class brand_landing(RoutablePageMixin, Page):
    
    template = 'categorization/sub_page.html'
    # background_text = models.CharField(max_length=255, blank=True, null=True)
    # main_text = models.CharField(max_length=255)
    # brief = models.CharField(max_length=20000, blank=True, null=True)
    # # brief_part2 = TextBlock(required=False)
    # image = models.ForeignKey(
    #     'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    # )
    brand = models.ForeignKey(to=brand_models.models.Brand, on_delete=models.CASCADE, related_name="brand_landing_page")
    header_sec = StreamField([("intro_with_background", intro_with_background())], max_num=1, min_num=1)

    image_logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('brand'),
        FieldPanel('header_sec'),
        FieldPanel('image_logo')
    ]

    def get_context(self, request, *args, **kwargs):
        ctx =  super().get_context(request, *args, **kwargs)
        # parent = self.cat.parent
        # siblings = parent.get_descendants(include_self=True)
        cats_ids = prod_models.models.Product.objects.filter(Q(brand=self.brand)).values("category").distinct()
        cats_children = CategoryMp.objects.filter(id__in=cats_ids)
        cats = CategoryMp.objects.filter(Q(id__in=cats_ids) | Q(id__in=cats_children.values('parent_id')))
        # brands = prod_models.models.Product.objects.filter(Q(category=self.cat)).values("brand").distinct()
        # brand_pages = brand_models.pages.BrandsDetailPage.objects.filter(Q(brand__in=brands))
        product_pages = self.get_paginated_prods( self.get_prods())
        ctx["cats"] = cats
        print(cats)
        print('categories')
        # if brand_pages:
        #     ctx['brand_pages'] = brand_pages
        if product_pages:
            ctx["product_pages"] = product_pages
        print(ctx)
        return ctx

    def get_prods(self, additional_filters={}):
        
        products = prod_models.models.Product.objects.filter(Q(brand=self.brand))
        print(additional_filters)
        # if additional_filters.get('brand', None):
        #     print(additional_filters['brand'])
        #     print("lol")
        #     products = products.filter(Q(brand__name=additional_filters['brand']))
        products = products.values("id").distinct()
        print(products)
        return prod_models.pages.productDetailPage.objects.filter(product__in=products)

    def get_paginated_prods(self, qs, page=None):
        paginator = Paginator(qs, 3)
        # page = 1

        try:
            posts = paginator.page(page)
            print(posts.number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.object_list.none()
        return posts
    

    @re_path(r'^products/$', name="products")
    def next_page(self, request,):
        # brand = request.Grequest.GET.get('brand', None)
        # print(brand)
        additional_filters = {}
        brand = request.GET.get('brand', None)
        print(f"brand{brand}")
        if brand:
            print(additional_filters)
            additional_filters['brand'] = brand
            
        return self.render(
            request,
            context_overrides={"query":{"brand":brand if brand else None},
                'product_pages': self.get_paginated_prods(self.get_prods(additional_filters=additional_filters), request.GET.get('pages', 1)
) ,
            },
            template="categorization/paginated_cat_prods.html",
        )
