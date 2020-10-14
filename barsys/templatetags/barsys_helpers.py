import locale
from re import sub as re_sub

from bootstrap3.templatetags.bootstrap3 import bootstrap_icon
from django import template
from django.conf import settings
from django.core.validators import URLValidator, ValidationError
from django.utils import formats

register = template.Library()


@register.simple_tag
def bicon(icon):
    """ Icon shortcut with easily changable default icon size """
    return bootstrap_icon(icon, extra_classes="gi-1p5x")


@register.simple_tag
def bool_to_icon(value):
    if value:
        return bicon("ok")
    else:
        return bicon("remove")


def get_locale_str():
    """ Please tell me how to do this the right way """
    l = settings.LANGUAGE_CODE
    l_split = l.split('-')
    l = l_split[0].lower() + "_" + l_split[1].upper() + ".UTF-8"

    return l


@register.filter(name='currency')
def currency(value):
    if not value:
        value = 0

    locale.setlocale(locale.LC_ALL, get_locale_str())
    return locale.currency(value, grouping=True)



@register.filter()
def comment_url_enhancement(value):
    validate = URLValidator()
    try:
        validate(value)
        return "<a href=\"" + value + "\">" + value + "</a>"
    except ValidationError as exception:
        return value


@register.filter
def keyvalue(dict, key):
    return dict.get(key, '')


@register.filter
def sdatetime(value):
    return formats.date_format(value, "SHORT_DATETIME_FORMAT")


@register.filter
def sdate(value):
    return formats.date_format(value, "SHORT_DATE_FORMAT")


@register.filter
def clean_str(instr):
    # clean string and only leave characters compatible with SEPA

    replace_dict = {
        "ä": "ae", "Ä": "Ae", "ö": "oe", "Ö": "Oe", "ü": "ue", "Ü": "Ue", "ß": "ss",
        '"': "-", "'": "-"
    }
    result_str = instr
    for k, v in replace_dict.items():
        result_str = result_str.replace(k, v)

    result_str = re_sub(r'[^A-Za-z0-9 .,\-+]+', '', result_str)

    return result_str
