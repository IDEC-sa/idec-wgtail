from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock

from banner.blocks import BodyBlock_banners
from idec.blocks import intro_with_background
from categorization.models.blocks import BlogsContenet



# ------------------------------------------


# class ProductContenet(StreamBlock):
class ProductContenet(StreamBlock):
    product = PageChooserBlock(required=True, page_type='product.productDetailPage')

class Products(StructBlock):
    # intro_with_background = intro_with_background()
    productContenet=ProductContenet(required = True)


# class BlogsContenet(StreamBlock):
class Products(StructBlock):
    # intro_with_background = intro_with_background()
    productContenet=ProductContenet(required = True)





# الكتلة الرئيسية التي تحتوي على جميع المكونات
class BodyBlock_product(StreamBlock):
    h1 = CharBlock()
    # bodyBlock_banners = BodyBlock_banners()  # إضافة كتلة المشروع
    productContenet = ProductContenet()
    intro_with_background_ = intro_with_background()
    blogsContenet = BlogsContenet()





# --------------------------------------------------------------------------------------
























