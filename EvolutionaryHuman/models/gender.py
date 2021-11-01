import typing

from .base import GenderBase


__all__ = ("Gender", "genders")


genders = ("male", "female", "non-binary", "genderless")


class Gender(GenderBase):
    _type: str

    def __init__(self, gender: str) -> typing.NoReturn:
        """
        Parameters
        ----------
        gender: str
        """
        assert (
            gender in genders
        ), f"Invalid gender {gender!r}! Try one of these: {', '.join(genders)}"
        self._type = gender

    @property
    def type(self) -> str:
        """
        Returns
        -------
        str
        """
        return self._type

    __str__: typing.Callable[[object], str] = lambda self: self.type
