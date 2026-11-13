from decimal import Decimal, ROUND_HALF_UP

from django import template

register = template.Library()


@register.filter
def clp(value):
    amount = Decimal(str(value)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return f'{amount:,.0f}'.replace(',', '.')
