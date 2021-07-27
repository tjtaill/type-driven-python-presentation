from typing import IO, Union, overload, Literal

# from typing_extensions import Literal # pre 3.8 so 3.7 and lower


modes = Union[
    Literal["r"],
    Literal["rb"],
    Literal["w"],
    Literal["wb"],
]

text_modes = Union[Literal["r"], Literal["w"]]

binary_modes = Union[Literal["rb"], Literal["wb"]]


@overload
def open_file(file_path: str, mode: text_modes) -> IO[str]:  # type: ignore
    pass


@overload
def open_file(file_path: str, mode: binary_modes) -> IO[bytes]:  # type: ignore
    pass


def open_file(file_path: str, mode: modes) -> Union[IO[str], IO[bytes]]:
    return open(file_path, mode)


open_file("foo.txt", "bar")  # will not type check bar not valid literal
tf = open_file("foo.txt", "w")
tf.write(b"foo bar as bytes")  # fails to type check
tf.write("foo bar as str")  # type checks write string in text mode
tf.close()
bf = open_file("bar.bin", "wb")
bf.write("bar as str")  # fails to type check
bf.write(b"bar as bytes")  # type check ok write bytes in binary mode
bf.close()
