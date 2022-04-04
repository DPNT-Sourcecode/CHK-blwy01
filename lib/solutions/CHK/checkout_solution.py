# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


def checkout(skus):
    if not isinstance(skus, str):
        return -1
    total = 0
    basket = Counter(skus)
    while True:
        mixed_purchase = [k for k in basket.keys() if k in mixed_offers[0]]
        if len(mixed_purchase) >= mixed_offers[1]:
            remove = mixed_offers[1]
            total += mixed_offers[2]
            for s in sorted(
                mixed_purchase,
                key=lambda x: price_table[x],
                reverse=True,
            ):
                while remove > 0 and basket[s] > 0:
                    remove -= 1
                    basket[s] -= 1
                    if basket[s] == 0:
                        basket.pop(s)
        else:
            break
    for sku, number in basket.items():
        try:
            price = price_table[sku]
        except KeyError:
            return -1
        if sku in get_free_offers:
            qualify_sku = get_free_offers[sku][0]
            get_free_multiplayer = get_free_offers[sku][1]
            if sku == qualify_sku:
                number -= basket[qualify_sku] // (get_free_multiplayer + 1)
            else:
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


price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

multibuy_offers = {
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    "H": {5: 45, 10: 80},
    "K": {2: 120},
    "P": {5: 200},
    "Q": {3: 80},
    "V": {2: 90, 3: 130},
}

get_free_offers = {
    "B": ("E", 2),
    "F": ("F", 2),
    "M": ("N", 3),
    "Q": ("R", 3),
    "U": ("U", 3),
}

mixed_offers = ({"S", "T", "X", "Y", "Z"}, 3, 45)

