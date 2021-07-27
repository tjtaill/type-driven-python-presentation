from typing import Any


def untyped_function(foo) -> Any:
    return foo


def polluted_function(foo):
    return untyped_function(foo)
