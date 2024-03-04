from django import template


register = template.Library()


@register.inclusion_tag('partials/previous_and_next_case_buttons.html')
def previous_and_next_case_buttons(page_obj, request):
    return {'page_obj': page_obj, 'request': request}


@register.inclusion_tag('partials/only_previous_case_buttons.html')
def only_previous_case_buttons(page_obj, request):
    return {'page_obj': page_obj, 'request': request}


@register.inclusion_tag('partials/only_next_case_buttons.html')
def only_next_case_buttons(page_obj, request):
    return {'page_obj': page_obj, 'request': request}
