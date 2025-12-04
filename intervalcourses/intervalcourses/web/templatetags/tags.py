from django import template

from web.models import Configuration

register = template.Library()


@register.simple_tag
def get_value(key):
    if Configuration.objects.filter(key=key).exists():
        return Configuration.objects.filter(key=key).first().value
    else:
        return ""
