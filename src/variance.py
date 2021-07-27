from typing import Callable, Tuple, FrozenSet, List, Set


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class D(C):
    pass


class E(D):
    pass


def foo(c: C) -> B:
    return B()


def bar(d: D) -> D:
    return D()


# why does this type check ?
# foo can be assigned to callable because it provides >= in the return type
# and requires <= in terms of arguments
f: Callable[[C | D | E], A | B] = foo
"""
doesn't type check bar return type is more general(ized) than callable signature
also bar argument is more specialized/specific than the callable signature argurments
to fix need to change to Callable[[D|E], A|B|C|D]
"""
e: Callable[[A | B | C], E] = bar

# tuples are read only therefore are safe to be covariant
t1: Tuple[B, C] = (D(), C())
t2: Tuple[A, B] = t1  # this works because tuples are read only and covariant

# frozenset also read only so covariant because they are read only
fs1: FrozenSet[B] = frozenset([B(), D(), C()])
fs2: FrozenSet[A] = fs1  # this works because frozenset is read only so covariant

# sets are invariant because they are read write
s1: Set[B] = {B()}
s2: set[A] = s1  # fails to type check and not safe to write into collection
s3: Set[B] = s1  # only assignable to exactly same type

# list, set and dict are both read and write so are therefore invariant
lb: List[B] = [C()]
la: List[
    A
] = lb  # won't type check because invariant as a read/write container should be
