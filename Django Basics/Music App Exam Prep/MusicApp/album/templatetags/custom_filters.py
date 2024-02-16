from django.template import Library

register = Library()


@register.filter(name='format_price')
def format_price(value):
    try:
        return f'{float(value):.2f}'
    except ValueError:
        return value
