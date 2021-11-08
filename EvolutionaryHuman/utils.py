import math
import typing

from random import (
    choice,
    choices,
    seed as set_random_seed,
)

from .data import (
    get_names,
    FILE_FEMALE,
    FILE_MALE,
    FILE_NEUTRAL,
)
from .models.base import GenderBase
from .models import (
    Gender,
    Person,
    Sexuality,
)


__all__ = (
    "set_random_seed",
    "age_occurrence",
    "iq_occurrence",
    "get_random_age",
    "get_random_name",
    "get_random_iq",
    "get_random_gender",
    "get_random_sexuality",
    "generate_random_person",
)


def age_occurrence(
    age: float,
    /,
) -> float:
    """
    Source of the formula:
    logistical regression with following data: (more in /tools/ages)
    https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_Population/WPP2019_POP_F15_1_ANNUAL_POPULATION_BY_AGE_BOTH_SEXES.xlsx
    (TABLE: estimates; INDEX: 71; World from 2020)

    Parameters
    ----------
    age: float

    Returns
    -------
    float
    """
    return 6.38521e8 / (1 + 0.006612 * math.e ** (0.08492 * age))


AGE_RANGE_FROM_0_TO_120: list[float] = [age_occurrence(i) for i in range(0, 120 + 1)]


def iq_occurrence(
    iq: float,
    /,
    *,
    sigma: float = 15,
    mu: float = 100,
) -> float:
    """
    Source of the formula:
    https://online.stat.psu.edu/stat414/book/export/html/713

    Parameters
    ----------
    iq: float
    sigma, mu: float
        The σ (sigma)/μ (mu) for the formula.

    Returns
    -------
    float
    """
    return (
        1
        / (sigma * math.sqrt(2 * math.pi))
        * math.exp(-(1 / 2) * ((iq - mu) / sigma) ** 2)
    )


IQ_RANGE_FROM_40_TO_160_SIGMA_15_MU_100: list[float] = [
    iq_occurrence(i) for i in range(40, 160 + 1)
]


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

    return choices(
        range(lower_bound, upper_bound + 1),
        occurrences,
    )[0]


def get_random_name(
    *,
    gender: typing.Union["GenderBase", str] = "genderless",
) -> str:
    """
    Gets a name and respects the gender

    Parameters
    ----------
    gender: GenderBase, str

    Returns
    -------
    str
    """
    if isinstance(gender, str):
        gender = Gender(gender)

    assert isinstance(
        gender, GenderBase
    ), f"'gender' must be an instance of '.models.base.GenderBase' and not {gender.__class__.__name__!r}"

    if gender.type == "female":
        return choice(NAMES_FEMALE)
    if gender.type == "male":
        return choice(NAMES_MALE)
    return choice(NAMES_NEUTRAL)


NAMES_FEMALE: list[str] = get_names(category=FILE_FEMALE)
NAMES_MALE: list[str] = get_names(category=FILE_MALE)
NAMES_NEUTRAL: list[str] = get_names(category=FILE_NEUTRAL)


def get_random_iq(
    *,
    lower_bound: int = 40,
    upper_bound: int = 160,
    sigma: float = 15,
    mu: float = 100,
) -> int:
    """
    Creates a random iq based on the formula by:
    https://online.stat.psu.edu/stat414/book/export/html/713

    Parameters
    ----------
    lower_bound: int
        The minimum value for the return.
    upper_bound: int
        The maximum value for the return.
    sigma, mu: float
        The σ (sigma)/μ (mu) for the formula.

    Returns
    -------
    int
    """
    assert (
        lower_bound < upper_bound
    ), "'lower_bound' must be smaller than 'upper_bound'!"
    assert 0 < sigma and 0 < mu, "'sigma' and 'mu' must be positive!"

    occurrences: list[float] = (
        IQ_RANGE_FROM_40_TO_160_SIGMA_15_MU_100
        if lower_bound == 40 and upper_bound == 160 and sigma == 15 and mu == 100
        else [
            iq_occurrence(i, sigma=sigma, mu=mu)
            for i in range(lower_bound, upper_bound + 1)
        ]
    )

    return choices(
        range(lower_bound, upper_bound + 1),
        occurrences,
    )[0]


def get_random_gender() -> "Gender":
    """
    Creates a random gender based on data by:
    https://www.hrc.org/resources/2018-lgbtq-youth-report

    Returns
    -------
    Gender
    """
    return Gender(
        choices(GENDER_TYPES, GENDER_OCCURRENCE)[0],
    )


# fmt: off
GENDER_DISTRIBUTION: dict[str, float] = {
    # getting the percentage from around 80% to around 90%
    "male":         4.605 * 2,
    "female":       6.002 * 2,

    "non-binary":   1.461,
    "genderless":   1.109,
}
# fmt: on
GENDER_TYPES: tuple[str, ...] = ()
GENDER_OCCURRENCE: tuple[float, ...] = ()
for t, o in GENDER_DISTRIBUTION.items():
    GENDER_TYPES += (t,)
    GENDER_OCCURRENCE += (o,)
del t, o


def get_random_sexuality(
    *,
    gender: Gender,
) -> "Sexuality":
    """
    Creates a random sexuality based on data by:
    https://www.hrc.org/resources/2018-lgbtq-youth-report

    Parameters
    ----------
    gender: Gender

    Returns
    -------
    Sexuality
    """
    return Sexuality(
        choices(SEXUALITY_TYPES, SEXUALITY_OCCURRENCE)[0],
        gender,
    )


# fmt: off
SEXUALITY_DISTRIBUTION: dict[str, float] = {
    # 3/4th (24) of the sum (32)
    "heterosexual": 24.0,

    # a quarter (8) of the sum (32):
    "homosexual": 3.7,
    "bisexual": 3.4,
    "pansexual": 1.4,
    "asexual": .5
}
# fmt: on
SEXUALITY_TYPES: tuple[str, ...] = ()
SEXUALITY_OCCURRENCE: tuple[float, ...] = ()
for t, o in SEXUALITY_DISTRIBUTION.items():
    SEXUALITY_TYPES += (t,)
    SEXUALITY_OCCURRENCE += (o,)
del t, o


def generate_random_person(
    **person_kwargs,
) -> "Person":
    """
    Parameters
    ----------
    person_kwargs
        All arguments for the Person.
        If no are set random values 'll be used.

    Returns
    -------
    Person
    """
    # set required arguments
    person_kwargs.setdefault("iq", get_random_iq())
    person_kwargs.setdefault("gender", get_random_gender())
    person_kwargs.setdefault(
        "sexuality", get_random_sexuality(gender=person_kwargs["gender"])
    )
    person_kwargs.setdefault("name", get_random_name(gender=person_kwargs["gender"]))

    person = Person(**person_kwargs)

    if person.is_lgbtiq():
        # this change is made, 'cause it's statistically proven that
        # LGBTIQ+*-individuals are unhappier due to discrimination and hate
        person._happiness = (4 / 5) * person.happiness

    return person
