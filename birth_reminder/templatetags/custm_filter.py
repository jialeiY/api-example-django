from django import template

register=template.Library()

@register.filter(name='get_key')
def get_key(h,key):
    return h.get(key,None)
