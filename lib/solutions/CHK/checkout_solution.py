# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    total = 0
    basket = Counter(skus)
    for sku, number in basket.items():
        try:
            price = price_table[sku]
        except KeyError:
            return -1
        if sku in get_free_offers:
            qualify_sku = get_free_offers[sku][0]
            get_free_multiplayer = get_free_offers[sku][1]
            number -= basket[qualify_sku] // get_free_multiplayer
        if sku in multibuy_offers:
            for so_multiplayer in sorted(
                list(multibuy_offers[sku].keys()), reverse=True
            ):
                so_price = multibuy_offers[sku][so_multiplayer]
                so_items = number // so_multiplayer
                total += so_items * so_price
                number = number % so_multiplayer
        total += price * number
    return total


price_table = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

multibuy_offers = {"A": {3: 130, 5: 200}, "B": {2: 45}}

get_free_offers = {"B": ("E", 2), "F": ("F", 2)}


