# Using phantom types for compile time/typecheck time type safe state machine
from typing import Generic, TypeVar


class Received:
    pass


class Validated:
    pass


class Processed:
    pass


class Sanitized:
    pass


class Sent:
    pass


S = TypeVar("S", Received, Validated, Processed, Sanitized, Sent)
D = TypeVar("D")


class Data(Generic[S, D]):
    def __init__(self, value: D):
        self.value = value


def receive(value: D) -> Data[Received, D]:
    return Data(value)


def validate(data: Data[Received, D]) -> Data[Validated, D]:
    return Data(data.value)


def process(data: Data[Validated, D]) -> Data[Processed, D]:
    return Data(data.value)


def sanitize(data: Data[Processed, D]) -> Data[Sanitized, D]:
    return Data(data.value)


def send(data: Data[Sanitized, D]) -> Data[Sent, D]:
    return Data(data.value)


d = receive(42)
vd: Data[Validated, int] = validate(d)
pd: Data[Processed, int] = process(vd)
sd: Data[Sanitized, int] = sanitize(
    vd
)  # doesn't type check expects Processed state not Validated state
