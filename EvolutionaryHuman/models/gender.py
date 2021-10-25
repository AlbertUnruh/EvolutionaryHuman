from .base import Base


__all__ = (
    "Gender",
    "genders"
)


genders = ("male", "female", "non-binary", "genderless")


class Gender(Base):
    _type: str
    _slots_for_repr = ("type",)

    __slots__ = ()

    def __init__(self, gender):
        """
        Parameters
        ----------
        gender: str
        """
        assert gender in genders, f"Invalid gender {gender!r}! Try one of these: {', '.join(genders)}"
        self._type = gender

    @property
    def type(self):
        """
        Returns
        -------
        str
        """
        return self._type

    __str__ = lambda self: self.type  # noqa E731
