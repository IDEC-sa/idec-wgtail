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
    link = PageChooserBlock(required=False, page_type=None)  # يسمح باختيار أي صفحة وغير ملزم









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





# 

class ProjectsContenet(StreamBlock):
    project = PageChooserBlock(required=True, page_type='idec.ProjectDetailPage')

class Projects(StructBlock):
    intro_with_background = intro_with_background()
    projectsContenet=ProjectsContenet(required = True)

# 


class Projects(StructBlock):
    intro_with_background = intro_with_background()
    projectsContenet=ProjectsContenet(required = True)

# 

class Banner(StreamBlock):
    banner = PageChooserBlock(required=True, page_type='banner.BannerDetailPage')

# class ProductContenet(StreamBlock):
class ProductContenet(StreamBlock):
    product = PageChooserBlock(required=True, page_type='product.productDetailPage')

class Products(StructBlock):
    intro_with_background = intro_with_background()
    productContenet=ProductContenet(required = True)


# class BlogsContenet(StreamBlock):
class Products(StructBlock):
    intro_with_background = intro_with_background()
    productContenet=ProductContenet(required = True)


class BlogsContenet(StreamBlock):
    blog = PageChooserBlock(required=True, page_type='blog.blogDetailPage')

class Blogs(StructBlock):
    intro_with_background = intro_with_background()
    blogsContenet=BlogsContenet(required = True)

class Blogs(StructBlock):
    intro_with_background = intro_with_background()
    blogsContenet=BlogsContenet(required = True)



class FeedbacksBlock(StructBlock):
    title = CharBlock(required=True, max_length=100)
    rate = CharBlock(required=False, max_length=200)
    icon = CharBlock(required=False, max_length=200)



class Feedbacks(StreamBlock):
    feedback = FeedbacksBlock()
    intro_with_background = intro_with_background()
    # intro_with_background = intro_with_background()


 



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


class ServicesContenet(StreamBlock):
    service = PageChooserBlock(required=True, page_type='idec.serviesDetailPage')


class Services(StructBlock):
    intro_with_background = intro_with_background()
    services_contenets=ServicesContenet(required = True)



class career(StreamBlock):
    career = PageChooserBlock(required=True, page_type='idec.careerDetailPage')



class GalleryContenet(StreamBlock):
    category = PageChooserBlock(required=True, page_type="idec.CategoryPage")

class GalleryBlock(StructBlock):
    intro_with_background = intro_with_background()
    galleryContenet=GalleryContenet(required = True)





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
    banner = Banner()  # إضافة كتلة المشروع




class BranchBlock(StreamBlock):
    branch_name = CharBlock()



# --------------------------------------------------------------------------------------
























