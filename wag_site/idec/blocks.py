from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)

from wagtail.images.blocks import ImageChooserBlock





class SliderImage(StructBlock):

    catchy_text = TextBlock(required=False)
    text = TextBlock(required=False)
    dachedText = TextBlock(required=False)
    buttonText = TextBlock(required=False)
    buttonUrl = URLBlock(required=False)
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
    AboutUs = PageChooserBlock(required=True, page_type="about_us.aboutHome")









class Projects(StreamBlock):
    project = PageChooserBlock(required=True, page_type='idec.ProjectDetailPage')
    intro_with_background = intro_with_background()


class Products(StreamBlock):
    product = PageChooserBlock(required=True, page_type='product.productDetailPage')
    intro_with_background = intro_with_background()


class Blogs(StreamBlock):
    blog = PageChooserBlock(required=True, page_type='blog.blogDetailPage')
    intro_with_background = intro_with_background()



class FeedbacksBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    rate = CharBlock(required=False, max_length=200)
    icon = CharBlock(required=False, max_length=200)



class Feedbacks(StreamBlock):
    feedback = FeedbacksBlock()
    intro_with_background = intro_with_background()


 



class Aboutvideo(StructBlock):
    title = CharBlock(required=True, max_length=100)
    subtitle = CharBlock(required=False, max_length=200)
    image = ImageChooserBlock()
    link = CharBlock(required=False, max_length=200)

    button = CharBlock(required=False, max_length=200)
    AboutUs = PageChooserBlock(required=True, page_type="about_us.aboutHome")
    intro_with_background = intro_with_background()

    # detail_page = PageChooserBlock(required=False, page_type='idec.ProjectDetailPage')






# class ServiceBlock(StructBlock):
#     title = CharBlock(required=True, max_length=100)
#     sub_title = CharBlock(required=False, max_length=200)


# class Services(StreamBlock):
#     service = ServiceBlock()

class Services(StreamBlock):
    service = PageChooserBlock(required=True, page_type='idec.serviesDetailPage')
    intro_with_background = intro_with_background()



class career(StreamBlock):
    career = PageChooserBlock(required=True, page_type='idec.careerDetailPage')




class GalleryBlock(StreamBlock):
    category = PageChooserBlock(required=True, page_type="idec.CategoryPage")
    intro_with_background = intro_with_background()





class Brands(StreamBlock):
    brand = PageChooserBlock(required=True, page_type='brands.BrandsDetailPage')




# الكتلة الرئيسية التي تحتوي على جميع المكونات
class BodyBlock(StreamBlock):
    h1 = CharBlock()
    slider = Slider()
    about = HomeAboutBlock()
    projects = Projects()  # إضافة كتلة المشروع
    feedback = Feedbacks()
    aboutvideo = Aboutvideo()
    services = Services()  # إضافة كتلة المشروع
    gallery = GalleryBlock()
    career = career()  # إضافة كتلة المشروع
    blogs = Blogs()  # إضافة كتلة المشروع
    products = Products()  # إضافة كتلة المشروع
    brands = Brands()  # إضافة كتلة المشروع

class BranchBlock(StreamBlock):
    branch_name = CharBlock()



# --------------------------------------------------------------------------------------

























