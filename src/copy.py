from typing import TypeVar

from contravariance import WriteOnlyList, add
from covariance import ReadOnlyList, iterable
from hierarchy import A, B, C, D

T = TypeVar("T")


def flexible_typesafe_copy(rol: ReadOnlyList[T], wol: WriteOnlyList[T]) -> None:
    for t in iterable(rol):
        add(wol, t)


wolc: WriteOnlyList[C] = WriteOnlyList([C()])
wold: WriteOnlyList[D] = wolc  # ok contravariant
rold: ReadOnlyList[D] = ReadOnlyList([D()])
# type checks eventhough wold is pointing to a list of C
flexible_typesafe_copy(rold, wold)
flexible_typesafe_copy(rold, wolc)  # type checks
rolb: ReadOnlyList[B] = ReadOnlyList([B()])
flexible_typesafe_copy(rolb, wolc)  # doesn't type check not safe to copy B's to C's
wola: WriteOnlyList[A] = WriteOnlyList([])
flexible_typesafe_copy(rolb, wola)  # type checks safe to write B's to A's
flexible_typesafe_copy(ReadOnlyList[A]([]), wola)  # type check write A's to A's is good
# type checks safe to write D's to B's
flexible_typesafe_copy(rold, WriteOnlyList[B]([]))
