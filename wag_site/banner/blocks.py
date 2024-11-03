from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock













 



class Banners(StructBlock):
    title_b = CharBlock(required=True, max_length=100)
    subtitle_b = TextBlock(required=False, max_length=200)
    image_b = ImageChooserBlock()
    link_b = CharBlock(required=False, max_length=200)
    button_b = CharBlock(required=False, max_length=200)








# الكتلة الرئيسية التي تحتوي على جميع المكونات
class BodyBlock_banners(StreamBlock):
    h1 = CharBlock()
    banners = Banners()





# --------------------------------------------------------------------------------------


