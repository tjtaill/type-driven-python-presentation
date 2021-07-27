"""
Structural/Duck Typing vs Nominal Typing
Using pypi typing_extensions Protocol
"""
# from typing_extensions import Protocol # pre 3.8 pip install type_extensions
from typing import List, Protocol


class A:
    pass


# tradditional nominal subtyping inheritance
class B(A):
    pass


class C:
    pass


a: A = A()
b: A = B()
c: A = C()  # nominal type check failure

# structural subtyping
class SupportsApply(Protocol):
    def apply(self, img: List[List[int]]) -> dict:
        return {}


# notice Model doesn't need to inherit from SupportsApply
class Model:
    def apply(self, img: List[List[int]]) -> dict:
        return {}


class NotModel:
    def apply(self) -> None:
        pass


sa: SupportsApply = Model()  # type checks because shape of apply method matches
sa2: SupportsApply = NotModel()  # doesn't type check apply signature wrong
