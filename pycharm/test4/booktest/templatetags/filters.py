from django.template import Library

register = Library()  # 创建一个对象


@register.filter
def mod(value, value2):
    return value % value2 == 0
