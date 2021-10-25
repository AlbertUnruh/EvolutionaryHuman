
__all__ = (
    "Base",
)


class Base:
    _slots_for_repr: tuple[str]

    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, "_slots_for_repr"):
            raise RuntimeError(f"You need to set the attribute '_slots_for_repr' for the class {cls.__name__}!")

    def __str__(self):
        cls = self.__class__.__name__
        attrs = " ".join(f"{a}={self.__getattribute__(a)!r}" for a in self._slots_for_repr)
        if attrs:
            return f"<{cls}: {attrs}>"
        return f"<{cls}>"

    __repr__ = __str__
