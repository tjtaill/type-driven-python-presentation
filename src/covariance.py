from typing import Generic, TypeVar, List, Iterable
from hierarchy import A, B, C


T = TypeVar("T", covariant=True)
U = TypeVar("U")


class ReadOnlyList(Generic[T]):
    def __init__(self, elems: Iterable[T]) -> None:
        self.back_store: List[T] = [elem for elem in elems]


def iterable(rol: ReadOnlyList[U]) -> Iterable[U]:
    return iter(rol.back_store)


rolc: ReadOnlyList[C] = ReadOnlyList([C(), C()])
rola: ReadOnlyList[A] = rolc  # type checks because covariant
rolb: ReadOnlyList[B] = rola  # fails to typecheck A's are not B's
a: A = A()  # not legal to type annotate loop variables so must predeclare them
c: C = C()
# type checks only safe to read A's since could point to A's all the way down to bottom D's
for a in iterable(rola):
    pass
# doesn't type check only safe to read A's because mypy detect this pyright is silent
for c in iterable(rola):
    pass
