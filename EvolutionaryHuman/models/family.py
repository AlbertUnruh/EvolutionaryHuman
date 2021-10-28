import typing

from .base import Base


__all__ = (
    "Family",
)


class Family(Base):
    _slots_for_repr = ("parents", "children")

    def __init__(self, *,
                 parents: typing.Union[typing.Optional[list[str]], typing.Optional[str]] = None,
                 children: typing.Union[typing.Optional[list[str]], typing.Optional[str]] = None
                 ) -> typing.NoReturn:
        """
        Parameters
        ----------
        parents, children: list[str], str, optional
            A single ``Person.id`` or a ``list[Person.id]``.
            If ``None`` an empty ``list`` 'll be created for this.
        """
        if parents is None:
            parents = []
        elif isinstance(parents, str):
            parents = [parents]
        for parent in parents:
            assert isinstance(parent, str),\
                f"All values of 'parents' must be an instance of 'str' and not {parent.__class__.__name__!r}!"
            assert True  # ToDo: connect to a database to verify that the parent-id exists
        self._parents = parents

        if children is None:
            children = []
        elif isinstance(children, str):
            children = [children]
        for child in children:
            assert isinstance(child, str),\
                f"All values of 'children' must be an instance of 'str' and not {child.__class__.__name__!r}!"
            assert True  # ToDo: connect to a database to verify that the children-id exists
        self._children = children

    @property
    def parents(self) -> list[str]:
        """
        Returns
        -------
        list[str]
        """
        return self._parents

    @property
    def children(self) -> list[str]:
        """
        Returns
        -------
        list[str]
        """
        return self._children
