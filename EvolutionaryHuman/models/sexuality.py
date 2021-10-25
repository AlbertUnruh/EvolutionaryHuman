from .base import Base
from .gender import Gender


__all__ = (
    "Sexuality",
    "sexualities"
)


sexualities = ("heterosexual", "homosexual", "bisexual", "pansexual", "asexual")


class Sexuality(Base):
    _type: str
    _slots_for_repr = ("type",)

    __slots__ = ()

    def __init__(self, sexuality, gender):
        """
        Parameters
        ----------
        sexuality: str
        gender: Gender, str
            Needed for ``Sexuality.can_love()``.
        """
        assert sexuality in sexualities, f"Invalid sexuality {sexuality!r}! Try one of these: {', '.join(sexualities)}"
        self._type = sexuality

        if isinstance(gender, str):
            gender = Gender(gender)
        assert isinstance(gender, Gender), f"gender must be an instance of 'Gender', not {gender.__class__.__name__!r}!"
        self._gender = gender

    @property
    def type(self):
        """
        Returns
        -------
        str
        """
        return self._type

    def can_love(self, *, gender):
        """
        Notes
        -----
        If we are correct this makes no sense, because sexuality
        **is not** love and attraction. But since I'm not implementing
        romantic I make it this way.

        Parameters
        ----------
        gender: Gender, str

        Returns
        -------
        bool
        """
        if isinstance(gender, str):
            gender = Gender(gender)
        assert isinstance(gender, Gender), f"gender must be an instance of 'Gender', not {gender.__class__.__name__!r}!"

        if self.type == "heterosexual":
            return self._gender.type != gender.type

        if self.type == "homosexual":
            return self._gender.type == gender.type

        if self.type == "bisexual":
            # not the real definition of "bisexual", otherwise it would be equal
            # to "pansexual" or it must be noted which two genders are meant.
            return gender.type in ["male", "female"]

        if self.type == "pansexual":
            return True

        return False  # only "asexual" is left and is always False

    __str__ = lambda self: self.type  # noqa E731
