"""
Sum Types
Enum, Optional and Unions\
"""
from enum import Enum
from typing import Union, Optional, TypeVar


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


c: Color = Color.RED  # will type check
c1: Color = 3  # won't type check


def foo(val: Optional[str] = None) -> None:  # pre 3.10
    if val:  # without this check fails to type check
        print(val[:])


# Create my own union type
T = TypeVar("T")  # create generic type T with TypeVar
Result = Union[T, Exception]  # pre 3.10
Result1 = str | Exception  # post 3.10 unions can be defined with or |


def error_on_null(val: Optional[str]) -> Result[str]:
    if val:
        return val
    else:
        return ValueError("None is not accpetable")


r: Result[str] = error_on_null(None)
# notice python doesn't care that the name is different because it is Structural shape matches
r1: Result1 = error_on_null("Foo")

print(r[:])  # won't type check because doesn't no if it is a str or an Exception
# mypy/pyright understand isinstance but not type(r) == str this is a type guard
if isinstance(r, str):
    print(r[:])
else:
    print(r)

# python 3.10 match case mypy complains that it doesn't support this syntax, pypright support this
# match c: #
#     case Color.RED:
#         print("red")
#     case _:
#         print("not red")

# # structural pattern matching with match case
# s1: str | ValueError = ValueError("Foo")
# match s1:
#     case str():
#         print(s1[:]) # both pyright and mypy do not see this as type guarded
#     case ValueError():
#         print(type(s1))
