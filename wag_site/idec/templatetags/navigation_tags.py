from django import template

# import site:
from wagtail.models import Site

# from base.models import FooterText

register = template.Library()


# ... keep the definition of get_footer_text and add the get_site_root template tag:
@register.simple_tag(takes_context=True)
def get_site_root(context):
    print(Site.find_for_request(context["request"]).root_page)
    return Site.find_for_request(context["request"]).root_page

from django import template

from ..models import FooterText, Branch

@register.simple_tag()
def get_footer_text():
    branches = Branch.objects.filter(live=True)

    return {
        "branches": branches
    }
