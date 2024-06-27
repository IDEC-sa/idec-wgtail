from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock

class SliderImage(StructBlock):

    catchy_text = TextBlock()
    text = TextBlock()
    dachedText = TextBlock()
    buttonText = TextBlock()
    buttonUrl = URLBlock()
    image = ImageChooserBlock()

class Slider(StreamBlock):
    slide = SliderImage()

class intro_with_background(StructBlock):
    background_text = TextBlock()
    main_text = TextBlock()
    brief = TextBlock()

class main_info_client(StructBlock):
    main_text = TextBlock()
    description = TextBlock()

class main_info(StreamBlock):
    main_info_member = main_info_client()

class detailed_info_img(StructBlock):
    main_info = main_info()
    image = ImageChooserBlock()

class HomeAboutBlock(StreamBlock):
    main_info = main_info()
    intro_with_background = intro_with_background()

class BodyBlock(StreamBlock):
    h1 = CharBlock()
    slider = Slider()
    about = HomeAboutBlock()
