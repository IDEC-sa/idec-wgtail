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






class Block_header(StreamBlock):
    main_text = TextBlock()




# الكتلة الرئيسية التي تحتوي على جميع المكونات
class Bodycat(StreamBlock):
    h1 = CharBlock()
    block_header = Block_header()
    brands = Brands()



# --------------------------------------------------------------------------------------