from os import getcwd, chdir


__all__ = (
    "FILE_FEMALE",
    "FILE_MALE",
    "FILE_NEUTRAL",
    "get_file",
    "get_names",
)


__PATH__: str = __file__[::-1].split("/", 1)[1][::-1]
FILE_FEMALE: str = "./names/female.txt"
FILE_MALE: str = "./names/male.txt"
FILE_NEUTRAL: str = "./names/neutral.txt"


def get_file(
    file: str,
    /,
) -> str:
    """
    Parameters
    ----------
    file: str

    Returns
    -------
    str
    """
    cwd = getcwd()
    chdir(__PATH__)
    try:
        with open(file) as f:
            return f.read()
    finally:
        chdir(cwd)


def get_names(
    *,
    category: str = FILE_NEUTRAL,
) -> list[str]:
    """
    Parameters
    ----------
    category: str

    Returns
    -------
    list[str]
    """
    if category == "neutral":
        category = FILE_NEUTRAL
    elif category == "female":
        category = FILE_FEMALE
    elif category == "male":
        category = FILE_MALE

    if category not in {FILE_FEMALE, FILE_MALE, FILE_NEUTRAL}:
        raise ValueError(
            f"Invalid category {category!r}! Use on of them instead: 'female', 'male' and 'neutral'"
        )

    return get_file(category).splitlines()
