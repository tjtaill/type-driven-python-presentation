b: bool = True
b1: bytes = b"foo"
d: dict = {"answer": 42}
f: float = 3.14
f1: frozenset = frozenset({31, 37})
i: int = 42
l: list = ["Foo", "Bar"]
s: set = {31, 37}
s1: str = "Foo"
t: tuple = (31, 37)


class Bar:
    def __init__(self, value: str) -> None:
        self.value = value


bar: Bar = Bar("PJ's")
