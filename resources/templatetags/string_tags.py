from django import template

register = template.Library()


@register.simple_tag
def extract_tag_name(pathname):
    tag_name = pathname.split('/')[2]
    return tag_name.lower()
