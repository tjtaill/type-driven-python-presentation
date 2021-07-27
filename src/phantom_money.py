"""
Phantom Types
Technique to use types to constrain the space of correct programs even further
"""
from typing import Generic, TypeVar


class Usd:
    pass


class Cdn:
    pass


T = TypeVar("T", Usd, Cdn)


class Money(Generic[T]):
    def __init__(self, value: int):
        self.value = value


def add(m1: Money[T], m2: Money[T]) -> Money[T]:
    return Money(m1.value + m2.value)


m1: Money[Cdn] = Money(500)
m2: Money[Usd] = Money(1000)
m3: Money[Cdn] = Money(250)
m4: Money[Cdn] = add(m1, m2)  # doesn't type check usd and cdn can't be added
m5: Money[Cdn] = add(m1, m3)  # type checks cdn can be added to cdn
