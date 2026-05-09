import markdown as md

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
@stringfilter
def markdown_filter(value):
    html = md.markdown(
        value,
        extensions=[
            "fenced_code",
            "codehilite",
            "toc",
        ],
    )
    return mark_safe(html)
