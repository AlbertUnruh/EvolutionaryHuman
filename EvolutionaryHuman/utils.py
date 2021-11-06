import math

from random import (
    choices,
    seed as set_random_seed,
)


__all__ = (
    "set_random_seed",
    "age_occurrence",
    "get_random_age",
)


def age_occurrence(age: int, /) -> float:
    """
    Parameters
    ----------
    age: int

    Returns
    -------
    float
    """
    return 6.38521e8 / (1 + 0.006612 * math.e ** (0.08492 * age))


AGE_RANGE_FROM_0_TO_120: list[float] = [age_occurrence(i) for i in range(0, 120 + 1)]


def get_random_age(
    *,
    lower_bound: int = 0,
    upper_bound: int = 120,
) -> int:
    """
    Creates a random age based on the data by:
    https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_Population/WPP2019_POP_F15_1_ANNUAL_POPULATION_BY_AGE_BOTH_SEXES.xlsx
    (TABLE: estimates; INDEX: 71; World from 2020)

    Parameters
    ----------
    lower_bound: int
        The minimum value for the return.
    upper_bound: int
        The maximum value for the return.

    Returns
    -------
    int
    """
    assert (
        lower_bound < upper_bound
    ), "'lower_bound' must be smaller than 'upper_bound'!"

    occurrences: list[float] = (
        AGE_RANGE_FROM_0_TO_120
        if lower_bound == 0 and upper_bound == 120
        else [age_occurrence(i) for i in range(lower_bound, upper_bound + 1)]
    )
    res = lower_bound - 1

    while not lower_bound <= res <= upper_bound:
        res = choices(
            range(lower_bound, upper_bound + 1),
            occurrences,
        )[0]

    return res
