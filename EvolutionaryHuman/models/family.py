import typing

from .base import FamilyBase, PersonBase as Person


__all__ = ("Family",)


class Family(FamilyBase):
    _parents: list[str]
    _children: list[str]

    def __init__(
        self,
        *,
        parents: typing.Optional[
            typing.Union[list[str], str, list["Person"], "Person"]
        ] = None,
        children: typing.Optional[
            typing.Union[list[str], str, list["Person"], "Person"]
        ] = None,
    ) -> typing.NoReturn:
        """
        Parameters
        ----------
        parents, children: list[str], str, list[Person], Person, optional
            A single ``Person.id`` or a ``list[Person.id]`` (you can also pass just ``Person``).
            If ``None`` an empty ``list`` 'll be created for this.
        """
        self._parents = []
        if parents is None:
            parents = []
        elif isinstance(parents, (str, Person)):
            parents = [parents]
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
            self._parents.append(parent)

        self._children = []
        if children is None:
            children = []
        elif isinstance(children, (str, Person)):
            children = [children]
        for child in children:
            assert isinstance(child, (str, Person)), (
                f"All values of 'children' must be an instance of 'str' "
                f"or '.models.base.PersonBase' and not {child.__class__.__name__!r}!"
            )
            if isinstance(child, Person):
                child = child.id
            assert True  # ToDo: connect to a database to verify that the children-id exists
            self._children.append(child)

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
