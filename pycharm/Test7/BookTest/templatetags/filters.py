from django.template import Library

register = Library()


@register.filter
def mod1(vaule):
    return vaule % 3 == 0
