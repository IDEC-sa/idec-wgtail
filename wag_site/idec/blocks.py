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


class HomeAboutBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    main_info = main_info()
    intro_with_background = intro_with_background()




 



# كتلة المشروع
class ProjectBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    subtitle = CharBlock(required=False, max_length=200)
    image = ImageChooserBlock()
    description = RichTextBlock()
    start_date = DateTimeBlock()
    end_date = DateTimeBlock()
    clients = CharBlock(required=False, max_length=200)
    area = CharBlock(required=False, max_length=100)
    project_year = CharBlock(required=False, max_length=4)
    project_type = CharBlock(required=False, max_length=100)
    detail_page = PageChooserBlock(required=False, page_type='idec.ProjectDetailPage')


class Projects(StreamBlock):
    project = ProjectBlock()


class FeedbacksBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    rate = CharBlock(required=False, max_length=200)
    icon = CharBlock(required=False, max_length=200)



class Feedbacks(StreamBlock):
    feedback = FeedbacksBlock()


 



class Aboutvideo(StructBlock):
    title = CharBlock(required=True, max_length=100)
    subtitle = CharBlock(required=False, max_length=200)
    image = ImageChooserBlock()
    link = CharBlock(required=False, max_length=200)

    button = CharBlock(required=False, max_length=200)

    # detail_page = PageChooserBlock(required=False, page_type='idec.ProjectDetailPage')






class ServiceBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    sub_title = CharBlock(required=False, max_length=200)


class Services(StreamBlock):
    service = ServiceBlock()










# الكتلة الرئيسية التي تحتوي على جميع المكونات
class BodyBlock(StreamBlock):
    h1 = CharBlock()
    slider = Slider()
    about = HomeAboutBlock()
    projects = Projects()  # إضافة كتلة المشروع
    feedback = Feedbacks()
    aboutvideo = Aboutvideo()
    services = Services()  # إضافة كتلة المشروع

class BranchBlock(StreamBlock):
    branch_name = CharBlock()
