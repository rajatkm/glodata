from django import template

register = template.Library()

@register.inclusion_tag('render_feedentry.html')
def render_feedentry(feedentry):
    return {'feedentry': feedentry}