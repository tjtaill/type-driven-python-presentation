from typing import Dict, List, Set, Tuple  # python 3.8 and lower requires to use this

d: Dict[str, int] = {"answer": 42}  # python pre 3.9 way
d1: dict[str, int] = {
    "answer": 42
}  # python 3.9 allows you to use the collection type itself
l: List[str] = ["Foo", "Bar"]
l1: list[str] = ["Foo", "Bar"]
s: Set[int] = {31, 37}
s1: set[int] = {31, 37}
t: Tuple[int, int] = (31, 37)
t1: tuple[int, int] = (31, 37)

d["johny 5"] = "is alive"  # type error this would work with untyped dict
