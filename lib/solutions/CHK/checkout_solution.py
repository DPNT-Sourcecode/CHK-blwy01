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
        if sku in special_offers:
            for so_multiplayer in sorted(list(special_offers[sku].keys()), reverse=True):
                so_price = special_offers[sku][so_multiplayer]
                so_items = number // so_multiplayer
                total += (so_items * so_price)
                number = number % so_multiplayer
        total += (price * number)
    return total


price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

special_offers = {"A": {3: 130, 5: 200}, "B": {2: 45}}
