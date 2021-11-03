import abc
import typing

__all__ = (
    "Base",
    "FamilyBase",
    "GenderBase",
    "PersonBase",
    "SexualityBase",
)


_classes_type = typing.ClassVar[
    dict[
        str,
        typing.Type[
            object,
        ],
    ]
]


class Base(abc.ABC):
    """
    BaseClass where all models inherit from.

    Notes About The Class
    ---------------------
    This class provides the methods ``__repr__`` and ``__str__`` to have a nice
    looking representation for all models by default. ``__str__`` might be
    overridden by some models when they just store "basic" values.
    """

    _slots_for_repr: typing.Iterable[str]

    @abc.abstractmethod
    def __init__(self, *args, **kwargs) -> typing.NoReturn:
        ...

    def __init_subclass__(cls) -> typing.NoReturn:
        """validates new subclasses"""
        # slots for __repr__ and __str__
        if not hasattr(cls, "_slots_for_repr"):
            raise RuntimeError(
                f"You need to set the attribute '_slots_for_repr' for the class {cls.__name__}!"
            )
        for attr in cls._slots_for_repr:
            if not hasattr(cls, attr):
                raise RuntimeError(
                    f"You need to set the attribute '{attr}' for the class {cls.__name__}!"
                )

        # setup
        if hasattr(cls, "_classes"):
            assert isinstance(cls._classes, dict), (
                f"If you provide the attribute '_classes' it must be a dict "
                f"and not {cls._classes.__class__.__name__!r}!"
            )
            assert getattr(getattr(cls, "setup", None), "__self__", None) is cls, (
                f"You must provide the ***classmethod*** 'setup' if you provide "
                f"the attribute '_classes'!"
            )
            if abc.ABC not in cls.__bases__:
                if (
                    not getattr(getattr(cls, "setup_missing", None), "__self__", None)
                    is cls
                ):
                    import sys

                    print(
                        f"It's recommended to add the ***classmethod setup_missing*** "
                        f"to the class {cls.__name__}.",
                        file=sys.stderr,
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
    """
    BaseClass for the family model.
    """

    _slots_for_repr = {
        "parents",
        "children",
    }

    @property
    @abc.abstractmethod
    def parents(self) -> list[str]:
        """
        - all parents ids
        """

    @property
    @abc.abstractmethod
    def children(self) -> list[str]:
        """
        - all children ids
        """


class GenderBase(Base, abc.ABC):
    """
    BaseClass for the gender model.
    """

    _slots_for_repr = {
        "type",
    }

    @property
    @abc.abstractmethod
    def type(self) -> str:
        """
        - the gender
        """

    __str__: typing.Callable[[object], str] = lambda self: self.type


class PersonBase(Base, abc.ABC):
    """
    BaseClass for the person model.
    """

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

    _classes: _classes_type = {"family": Base}

    @classmethod
    def setup(
        cls,
        *,
        family_cls: typing.Type[FamilyBase] = None,
    ) -> typing.NoReturn:
        """
        Sets the classes for Person up.

        Parameters
        ----------
        family_cls: typing.Type[FamilyBase], optional
            The class witch is used to create instances of the class.
        """
        if family_cls is not None:
            assert issubclass(
                family_cls, FamilyBase
            ), "'family_cls' must be a type of '.models.base.FamilyBase'!"
            cls._classes["family"] = family_cls

    @classmethod
    def setup_missing(
        cls,
    ) -> list:
        missing = []
        for key in cls._classes:
            if abc.ABC in cls._classes[key].__bases__:
                missing.append(key)
        return missing

    @property
    @abc.abstractmethod
    def happiness(self) -> float:
        """
        - 0.0 <= HAPPINESS <= 1.0
        - 1.0 -> max happiness
        """

    @property
    @abc.abstractmethod
    def hunger(self) -> float:
        """
        - 0.0 <= HUNGER <= 1.0
        - 1.0 -> max hunger
        """

    @property
    @abc.abstractmethod
    def in_love(self) -> typing.Optional["PersonBase"]:
        """
        - no love -> None
        - in love -> PersonBase
        """

    @property
    @abc.abstractmethod
    def married(self) -> typing.Optional["PersonBase"]:
        """
        - not married -> None
        - married -> PersonBase
        """

    @property
    @abc.abstractmethod
    def pregnant(self) -> bool:
        """
        - pregnant -> True
        - not pregnant -> False
        """

    @property
    @abc.abstractmethod
    def gender(self) -> "GenderBase":
        """
        - GenderBase(GENDER) <- means an instance of the class
        """

    @property
    @abc.abstractmethod
    def sexuality(self) -> "SexualityBase":
        """
        - SexualityBase(SEXUALITY) <- means an instance of the class
        """

    @property
    @abc.abstractmethod
    def age(self) -> int:
        """
        - 0 <= AGE
        """

    @property
    @abc.abstractmethod
    def money(self) -> float:
        """
        - 0.0 <= MONEY
        """

    @property
    @abc.abstractmethod
    def iq(self) -> int:
        """
        - 0 <= IQ
        """

    @property
    @abc.abstractmethod
    def family(self) -> "FamilyBase":
        """
        - FamilyBase(SEXUALITY) <- means an instance of the class
        """

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        *should be clear what this is...*
        """

    @property
    @abc.abstractmethod
    def id(self) -> str:
        """
        - unique == True
        """

    @property
    @abc.abstractmethod
    def alive(self) -> bool:
        """
        - alive -> True
        - not alive -> False
        """

    @property
    @abc.abstractmethod
    def dead(self) -> bool:
        """
        - not alive
        """

    @classmethod
    @abc.abstractmethod
    def create_person(cls, *args, **kwargs) -> "PersonBase":
        """
        - create new Person
        - check id
        """


class SexualityBase(Base, abc.ABC):
    """
    BaseClass for the sexuality model.
    """

    _slots_for_repr = {
        "type",
    }

    _classes: _classes_type = {"gender": Base}

    @classmethod
    def setup(
        cls,
        *,
        gender_cls: typing.Type[GenderBase] = None,
    ) -> typing.NoReturn:
        """
        Sets the classes for Person up.

        Parameters
        ----------
        gender_cls: typing.Type[GenderBase], optional
            The class witch is used to create instances of the class.
        """
        if gender_cls is not None:
            assert issubclass(
                gender_cls, GenderBase
            ), "'gender_cls' must be a type of '.models.base.GenderBase'!"
            cls._classes["gender"] = gender_cls

    @classmethod
    def setup_missing(
        cls,
    ) -> list:
        missing = []
        for key in cls._classes:
            if abc.ABC in cls._classes[key].__bases__:
                missing.append(key)
        return missing

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        """
        - should take additionally the gender
        """

    @property
    @abc.abstractmethod
    def type(self) -> str:
        """
        - the sexuality
        """

    @abc.abstractmethod
    def can_love(self, *, gender: typing.Union[GenderBase, str]) -> bool:
        """
        - check if the own gender is able to love the other gender
        """

    __str__: typing.Callable[[object], str] = lambda self: self.type
