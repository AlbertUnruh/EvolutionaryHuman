import typing
import uuid

from .base import (
    PersonBase,
    FamilyBase as Family,
    GenderBase as Gender,
    SexualityBase as Sexuality,
)


__all__ = ("Person",)


class Person(PersonBase):
    """
    Represents a person.
    """

    _happiness: float
    _hunger: float
    _in_love: typing.Optional["Person"]
    _married: typing.Optional["Person"]
    _pregnant: bool
    _gender: "Gender"
    _sexuality: "Sexuality"
    _age: int
    _money: float
    _iq: int
    _family: "Family"
    _name: str
    _id: str
    _alive: bool

    def __init__(
        self,
        *,
        happiness: typing.Annotated[typing.SupportsFloat, "ValueRange[0., 1.]"] = 1,
        hunger: typing.Annotated[typing.SupportsFloat, "ValueRange[0., 1."] = 1,
        in_love: typing.Optional["Person"] = None,
        married: typing.Optional["Person"] = None,
        pregnant: bool = False,
        gender: "Gender",
        sexuality: "Sexuality",
        age: typing.Annotated[typing.SupportsInt, "MinVal[0]"] = 0,
        money: typing.Annotated[typing.SupportsFloat, "MinVal[0.]"] = 0.0,
        iq: typing.Annotated[typing.SupportsInt, "MinVal[0]"],
        family: typing.Optional["Family"] = None,
        name: typing.AnyStr,
        id: typing.Optional[typing.AnyStr] = None,  # noqa
        alive: bool = True,
    ) -> typing.NoReturn:
        """
        Parameters
        ----------
        # *must* be set
        gender: Gender
        sexuality: Sexuality
        iq: typing.SupportsInt
            Must be positive!
        name: typing.AnyStr

        # *can* be set, recommended
        happiness, hunger, money: typing.SupportsFloat
            Must be between ``0.0`` and ``1.0``!
        in_love, married: Person, optional
        pregnant: bool
        age: typing.SupportsInt
            Must be positive!
        family: Family, optional

        # *can* be set, not recommended
        id: typing.AnyStr, optional
        alive: bool
        """
        # first the required ones...
        assert isinstance(
            gender, Gender
        ), "'gender' must be an instance of '.models.base.GenderBase'!"
        self._gender = gender

        assert isinstance(
            sexuality, Sexuality
        ), "'sexuality' must be an instance of '.models.base.SexualityBase'!"
        self._sexuality = sexuality

        assert 0 <= (
            iq := int(iq)
        ), f"'iq' must be a value greater then 0 and not {iq!r}"
        self._iq = iq

        assert (name := str(name)), "'name' must be at least one character long!"
        self._name = name

        # second the optional, but recommended, ones...
        assert (
            0 <= (happiness := float(happiness)) <= 1
        ), f"'happiness' must be a value between 0 and 1 and not {happiness!r}!"
        self._happiness = happiness

        assert (
            0 <= (hunger := float(hunger)) <= 1
        ), f"'hunger' must be a value between 0 and 1 and not {hunger!r}"
        self._hunger = hunger

        assert 0 <= (
            money := float(money)
        ), f"'money' must be a value greater then 0 and not {money!r}"
        self._money = money

        assert (  # ToDo: person.can_love()
            isinstance(in_love, Person) or in_love is None
        ), "'in_love' must be an instance of '.models.base.PersonBase' or None!"
        self._in_love = in_love

        assert (  # ToDo: person.can_love()
            isinstance(married, Person) or married is None
        ), "'married' must be an instance of '.models.base.PersonBase' or None!"
        self._married = married

        assert (
            self.gender.type == "female" if (pregnant := bool(pregnant)) else True
        ), "Only persons where ``GenderBase.type == 'female'`` can get pregnant!"
        self._pregnant = pregnant

        assert 0 <= (
            age := int(age)
        ), f"'age' must be a value greater then 0 and not {age!r}"
        self._age = age

        assert (
            isinstance(family, Family) or family is None
        ), "'family' must be an instance of '.models.base.FamilyBase' or None!"
        self._family = family or __import__("family", None, None, ".").Family()

        # and last but not least the optional, but not recommended, ones...
        # ToDo: connect to a database to verify that the id is unique
        self._id = (
            str(id) or uuid.uuid4()
        )  # without assert, because empty IDs 'll be replaced

        self._alive = bool(alive)

    @classmethod
    def create_person(cls, *, replace_old: bool = False, **kwargs) -> "Person":
        """
        Parameters
        ----------
        replace_old: bool
            Whether an existing entry in the database should be replaced.
        kwargs
            The Arguments for the ``Person``.

        Returns
        -------
        Person

        Raises
        ------
        ValueError
            Raises if ``replace_old != True`` and the persons id already exists.
        """
        person = cls.__init__(**kwargs)
        # ToDo: connect to database to check for duplicates (persons id)
        # ToDo: connect to database to create entry
        return person

    @property
    def happiness(self) -> float:
        """
        Returns
        -------
        float
        """
        return self._happiness

    @property
    def hunger(self) -> float:
        """
        Returns
        -------
        float
        """
        return self._hunger

    @property
    def in_love(self) -> typing.Optional["Person"]:
        """
        Returns
        -------
        Person, optional
        """
        return self._in_love

    @property
    def married(self) -> typing.Optional["Person"]:
        """
        Returns
        -------
        Person, optional
        """
        return self._married

    @property
    def pregnant(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return self._pregnant

    @property
    def gender(self) -> Gender:
        """
        Returns
        -------
        Gender
        """
        return self._gender

    @property
    def sexuality(self) -> Sexuality:
        """
        Returns
        -------
        Sexuality
        """
        return self._sexuality

    @property
    def age(self) -> int:
        """
        Returns
        -------
        int
        """
        return self._age

    @property
    def money(self) -> float:
        """
        Returns
        -------
        float
        """
        return self._money

    @property
    def iq(self) -> int:
        """
        Returns
        -------
        int
        """
        return self._iq

    @property
    def family(self) -> Family:
        """
        Returns
        -------
        Family
        """
        return self._family

    @property
    def name(self) -> str:
        """
        Returns
        -------
        str
        """
        return self._name

    @property
    def id(self) -> str:
        """
        Returns
        -------
        str
        """
        return self._id

    @property
    def alive(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return self._alive

    @property
    def dead(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return not self.alive
