from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock

from banner.blocks import Banners








class intro_with_background(StructBlock):
    background_text = TextBlock()
    main_text = TextBlock()
    brief = TextBlock()

class main_info_client(StructBlock):
    main_text = TextBlock()
    description = TextBlock()

class main_info(StreamBlock):
    main_info_member = main_info_client()


class HomeAboutBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    main_info = main_info()
    intro_with_background = intro_with_background()










class FeedbacksBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    rate = CharBlock(required=False, max_length=200)
    icon = CharBlock(required=False, max_length=200)



class Feedbacks(StreamBlock):
    feedback = FeedbacksBlock()


 



class Aboutvideo(StructBlock):
    title = CharBlock(required=True, max_length=100)
    subtitle = TextBlock(required=False, max_length=200)
    image = ImageChooserBlock()
    link = CharBlock(required=False, max_length=200)

    button = CharBlock(required=False, max_length=200)






class AboutBanner(StructBlock):
    title = CharBlock(required=True, max_length=100)
    subtitle = TextBlock(required=False, max_length=200)
    back_title = CharBlock(required=False, max_length=200)

# Story

class AboutStory(StructBlock):
    title = CharBlock(required=True, max_length=100)
    description = TextBlock()
    image = ImageChooserBlock()



# class Banner(StreamBlock):
#     banner = PageChooserBlock(required=True, page_type='banner.BannerDetailPage')

# الكتلة الرئيسية التي تحتوي على جميع المكونات
class BodyBlock_about(StreamBlock):
    h1 = CharBlock()
    about = HomeAboutBlock()
    feedback = Feedbacks()
    aboutvideo = Aboutvideo()
    about_banner = AboutBanner()
    aboutstory = AboutStory()
    # banner = Banner()  # إضافة كتلة المشروع
    banners = Banners()


class BranchBlock(StreamBlock):
    branch_name = CharBlock()



# --------------------------------------------------------------------------------------


