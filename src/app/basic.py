from typing import Any, Final, TypeAlias


def foo(arg: Any) -> None:  # BASIC-any
    """BASIC - any"""
    pass


def foo_dict(x: dict[str, str]) -> None:  # BASIC-dict
    """BASIC - dict"""
    pass


def foo2(**kwargs: int | str) -> None:  # BASIC-kwargs
    """BASIC - kwargs"""
    pass


def foo3(x: list[str]) -> None:  # BASIC-list
    """BASIC - list"""
    pass


def foo4(x: int | None = None) -> None:  # BASIC-optional
    """BASIC - optional"""
    pass


def foo5(x: int) -> None:  # BASIC-parameter
    """BASIC - parameter"""
    pass


def foo6() -> int:  # BASIC-return
    """BASIC - return"""
    return 1


def foo7(x: tuple[str, int]) -> None:  # BASIC-tuple
    """BASIC - tuple"""
    pass


def foo8(x: str | int) -> None:  # BASIC-union
    """BASIC - union"""
    pass


Vector: TypeAlias = list[float]  # BASIC-typealias
my_list: Final[list[Any]] = []  # BASIC-final
a: int  # BASIC - variable
