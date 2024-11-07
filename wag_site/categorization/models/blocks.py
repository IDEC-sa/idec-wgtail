from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock

from banner.blocks import Banners
from wagtail.embeds.blocks import EmbedBlock
from wagtailvideos.blocks import VideoChooserBlock

from idec.blocks import Brands
from categorization.models.models import CategoryMp

# ------------------------------------------




class intro_with_background(StructBlock):
    background_text = TextBlock()
    main_text = TextBlock()
    brief = TextBlock(required=False)
    brief_part2 = TextBlock(required=False)
    image = ImageChooserBlock()





class Block_header(StructBlock):
    main_text = TextBlock()




class CategoryContenet(StreamBlock):
  
    category = PageChooserBlock(required=True, page_type="idec.CategoryPage")


class BrandContenet(StreamBlock):

    brand = PageChooserBlock(required=True, page_type='brands.BrandsDetailPage')



class ProductContenet(StreamBlock):
    product = PageChooserBlock(required=True, page_type='product.productDetailPage')




class BlogsContenet(StreamBlock):
    blog = PageChooserBlock(required=True, page_type='blog.blogDetailPage')




# الكتلة الرئيسية التي تحتوي على جميع المكونات
class Bodycat(StreamBlock):
    h1 = CharBlock()
    block_header = Block_header()
    brandContenet = BrandContenet()
    intro_header = intro_with_background()
    categoryContenet = CategoryContenet()
    productContenet = ProductContenet()
    blogsContenet = BlogsContenet()



# --------------------------------------------------------------------------------------