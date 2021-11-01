import abc
import typing

__all__ = (
    "Base",
    "FamilyBase",
    "GenderBase",
    "PersonBase",
    "SexualityBase",
)


class Base(abc.ABC):
    _slots_for_repr: typing.Iterable[str]

    @abc.abstractmethod
    def __init__(self, *args, **kwargs) -> typing.NoReturn:
        ...

    def __init_subclass__(cls, **kwargs) -> typing.NoReturn:
        if not hasattr(cls, "_slots_for_repr"):
            raise RuntimeError(
                f"You need to set the attribute '_slots_for_repr' for the class {cls.__name__}!"
            )
        for attr in cls._slots_for_repr:
            if not hasattr(cls, attr):
                raise RuntimeError(
                    f"You need to set the attribute '{attr}' for the class {cls.__name__}!"
                )

    def __str__(self) -> str:
        cls = self.__class__.__name__
        attrs = " ".join(
            f"{a}={self.__getattribute__(a)!r}" for a in self._slots_for_repr
        )
        if attrs:
            return f"<{cls}: {attrs}>"
        return f"<{cls}>"

    __repr__ = __str__


class FamilyBase(Base, abc.ABC):
    """Docs coming soon..."""

    _slots_for_repr = {
        "parents",
        "children",
    }

    @property
    @abc.abstractmethod
    def parents(self) -> list[str]:
        ...

    @property
    @abc.abstractmethod
    def children(self) -> list[str]:
        ...


class GenderBase(Base, abc.ABC):
    """Docs coming soon..."""

    _slots_for_repr = {
        "type",
    }

    @property
    @abc.abstractmethod
    def type(self) -> str:
        ...


class PersonBase(Base, abc.ABC):
    _slots_for_repr = {
        "happiness",
        "hunger",
        "in_love",
        "married",
        "pregnant",
        "gender",
        "sexuality",
        "age",
        "money",
        "iq",
        "family",
        "name",
        "id",
        "alive",
    }

    @property
    @abc.abstractmethod
    def happiness(self) -> float:
        ...

    @property
    @abc.abstractmethod
    def hunger(self) -> float:
        ...

    @property
    @abc.abstractmethod
    def in_love(self) -> typing.Optional["PersonBase"]:
        ...

    @property
    @abc.abstractmethod
    def married(self) -> typing.Optional["PersonBase"]:
        ...

    @property
    @abc.abstractmethod
    def pregnant(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def gender(self) -> "GenderBase":
        ...

    @property
    @abc.abstractmethod
    def sexuality(self) -> "SexualityBase":
        ...

    @property
    @abc.abstractmethod
    def age(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def money(self) -> float:
        ...

    @property
    @abc.abstractmethod
    def iq(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def family(self) -> "FamilyBase":
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def id(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def alive(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def dead(self) -> bool:
        ...


class SexualityBase(Base, abc.ABC):
    _slots_for_repr = {
        "type",
    }

    @property
    @abc.abstractmethod
    def type(self) -> str:
        ...

    @abc.abstractmethod
    def can_love(self, *, gender: typing.Union[GenderBase, str]) -> bool:
        ...
