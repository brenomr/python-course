"""
namedtyple - is a kind of tuple where each element has a name
and are immutable. useful to create simple classes, without
methods, only with attributes, or database records.

Are useful with data.

https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
"""
from collections import namedtuple
from typing import NamedTuple

# Portuguese for simplicity
Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['VALOR', 'NAIPE'])
as_espadas = Carta('A', 'espadas')

# More convenient to use
print(as_espadas.valor)
print(as_espadas.naipe)

# Instead of
print(as_espadas[0])
print(as_espadas[1])

for value in as_espadas:
    print(value)

print(as_espadas._fields)

# showing defaults
as_de_paus = Carta()
print(as_de_paus)


class Carta2(NamedTuple):
    valor: str
    naipe: str


valete_de_ouros = Carta2('J', 'ouros')

# We have the same access as the namedtuple from collections
print(valete_de_ouros.valor)
print(valete_de_ouros.naipe)
