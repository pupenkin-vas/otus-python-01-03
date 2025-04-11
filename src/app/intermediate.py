from collections.abc import Callable
from typing import (
    Awaitable,
    ClassVar,
    Iterable,
    Literal,
    LiteralString,
    NotRequired,
    Required,
    TypedDict,
    TypeVar,
    Unpack,
)

T = TypeVar("T")
T2 = TypeVar("T2", int, str)
T3 = TypeVar("T3", bound=int)
T4 = TypeVar("T4")
T5 = TypeVar("T5", bound=Callable)


class Foo:
    bar: ClassVar[int]  # INTERMEDIATE - class-var


class Foo2:
    bar: int  # INTERMEDIATE - instance-var


class Foo4:  # INTERMEDIATE - self
    def return_self(self: T4) -> T4:
        return self


class Student(TypedDict):  # INTERMEDIATE - typed-dict
    name: str
    age: int
    school: str


class Student2(TypedDict):  # INTERMEDIATE - typed-dict2
    name: str
    age: int
    school: NotRequired[str]


class Person(TypedDict, total=False):  # INTERMEDIATE - typed-dict3
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


class Person2(TypedDict):  # INTERMEDIATE - union
    name: str
    age: int


def foo(**kwargs: Unpack[Person2]) -> None:
    """INTERMEDIATE - union"""
    ...


def run_async(x: Awaitable[int]) -> None:  # INTERMEDIATE - await
    """INTERMEDIATE - await"""
    pass


def foo2(x: tuple[()]) -> None:  # INTERMEDIATE - tuple
    """INTERMEDIATE - tuple"""
    pass


def decorator(func: T5) -> T5:  # INTERMEDIATE - decorator
    """INTERMEDIATE - tuple"""
    return func


def add(a: T, b: T) -> T:  # INTERMEDIATE - generic
    """INTERMEDIATE - generic"""
    return a


def add2(a: T2, b: T2) -> T2:  # INTERMEDIATE - generic2
    """INTERMEDIATE - generic2"""
    return a + b


def add3(a: T3) -> T3:  # INTERMEDIATE - generic3
    """INTERMEDIATE - generic3"""
    return a


def foo3(
    direction: Literal["left", "right"],
) -> None:  # INTERMEDIATE - literal
    """INTERMEDIATE - literal"""
    pass


def execute_query(
    sql: LiteralString, parameters: Iterable[str] = ...
) -> None:  # INTERMEDIATE - literalstring
    """INTERMEDIATE - literalstring"""
    ...


SingleStringInput = Callable[[str], None]  # INTERMEDIATE - callable
