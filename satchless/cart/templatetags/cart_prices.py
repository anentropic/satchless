from django import template

from ...product.templatetags.product_prices import BasePriceNode, parse_price_tag

register = template.Library()

class CartItemPriceNode(BasePriceNode):
    def get_currency_for_item(self, item):
        return item.cart.currency

    def get_price(self, cartitem, currency, **kwargs):
        return cartitem.price(currency=currency, **kwargs)

class CartItemUnitPriceNode(BasePriceNode):
    def get_currency_for_item(self, item):
        return item.cart.currency

    def get_price(self, cartitem, currency, **kwargs):
        return cartitem.get_unit_price(currency=currency, **kwargs)

@register.tag
def cartitem_price(parser, token):
    try:
        return CartItemPriceNode(*parse_price_tag(parser, token))
    except (ImportError, NotImplementedError):
        pass
    return ''

@register.tag
def cartitem_unit_price(parser, token):
    try:
        return CartItemUnitPriceNode(*parse_price_tag(parser, token))
    except (ImportError, NotImplementedError):
        pass
    return ''
