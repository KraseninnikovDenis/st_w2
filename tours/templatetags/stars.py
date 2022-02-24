from django import template

register = template.Library()


@register.filter
def stars(count):
    return int(count) * "★"
