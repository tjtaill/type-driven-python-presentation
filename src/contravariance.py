from typing import TypeVar, Generic, Iterable, List
from hierarchy import B, C, D


T = TypeVar("T", contravariant=True)
U = TypeVar("U")  # invariant for writing safety


class WriteOnlyList(Generic[T]):
    def __init__(self, elems: Iterable[T]) -> None:
        self.back_store: List[T] = [elem for elem in elems]


# need to define a generic function outside class
# otherwise will interfere with assignability
def add(wol: WriteOnlyList[U], elem: U) -> None:
    wol.back_store.append(elem)


wolb: WriteOnlyList[B] = WriteOnlyList([B()])
wold: WriteOnlyList[D] = WriteOnlyList([D()])
# ok contravariant can point to C's, B'S or A's
wolc: WriteOnlyList[C] = wolb
# will not type check can only be as specific as C or more general
wolc2: WriteOnlyList[C] = wold
# doesn't type check only safe to write C's mypy detects this pyright doesn't
add(wolc, B())
# type checks contravariant collection safe to write C or higher
add(wolc, C())
