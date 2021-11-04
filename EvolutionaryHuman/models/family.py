import typing

from .base import FamilyBase, PersonBase as Person


__all__ = ("Family",)


_allowed_person_type = typing.Union[
    typing.Iterable[
        str,
    ],
    str,
    typing.Iterable[
        "Person",
    ],
    "Person",
]


class Family(FamilyBase):
    """
    Represents a family.
    """

    _parents: set[str]
    _children: set[str]

    def __init__(
        self,
        *,
        parents: typing.Optional[_allowed_person_type] = None,
        children: typing.Optional[_allowed_person_type] = None,
    ) -> typing.NoReturn:
        """
        Parameters
        ----------
        parents, children: typing.Iterable[str], str, typing.Iterable[Person], Person, optional
            A single ``Person.id`` or a ``list[Person.id]`` (you can also pass just ``Person``).
            If ``None`` an empty ``list`` 'll be created for this.
        """
        self._parents = set()
        if parents is None:
            parents = set()
        elif isinstance(parents, (str, Person)):
            parents = {parents}
        for parent in parents:
            assert isinstance(parent, (str, Person)), (
                f"All values of 'parents' must be an instance of 'str' "
                f"or '.models.base.PersonBase' and not {parent.__class__.__name__!r}!"
            )
            if isinstance(parent, Person):
                parent = parent.id
            assert (
                True  # ToDo: connect to a database to verify that the parent-id exists
            )
            self._parents.add(parent)

        self._children = set()
        if children is None:
            children = set()
        elif isinstance(children, (str, Person)):
            children = {children}
        for child in children:
            assert isinstance(child, (str, Person)), (
                f"All values of 'children' must be an instance of 'str' "
                f"or '.models.base.PersonBase' and not {child.__class__.__name__!r}!"
            )
            if isinstance(child, Person):
                child = child.id
            assert True  # ToDo: connect to a database to verify that the children-id exists
            self._children.add(child)

    @property
    def parents(self) -> set[str]:
        """
        Returns
        -------
        set[str]
        """
        return self._parents

    @property
    def children(self) -> set[str]:
        """
        Returns
        -------
        set[str]
        """
        return self._children
