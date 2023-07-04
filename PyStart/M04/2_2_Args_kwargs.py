"""
**kwargs - zamienia podwojne argumenty na slowmnik
*args - zamienia ciag pojedynczych argumentow na krotke/tuple

"""


def log(*args, **kwargs):
    for arg in args:
        print(type(arg))
    print(args)  # (1, 2, 3)
    print(kwargs)  # {'hello': 'Seba'}


log(1, 2, 3, hello="Seba")



def get_brutto(netto, vat):
    return netto + netto * vat


values = [
    (100, 1.23),
    (50, 1.05)
]
# poniżej * oznacza wypakowanie krotki/tupli
for value in values:
    print(get_brutto(*value))
