# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

def checkout(skus):
    if not isinstance(skus, str):
        return -1
    total = 0
    try:
        basket = skus.split()
    except KeyError:
        return -1
    for sku in basket:
        total += price_table[sku]
    return total


price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

special_offers = {"A": (3, 130), "B": (2, 45)}


