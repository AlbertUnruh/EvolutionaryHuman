from .base import Base


__all__ = (
    "Family",
)


class Family(Base):
    _slots_for_repr = ()

    def __init__(self, *args, **kwargs):
        raise NotImplementedError
