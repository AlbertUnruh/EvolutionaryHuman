from os import getcwd, chdir, path


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
        if not path.isfile(file):
            raise NotImplementedError(
                f"Cannot find file {file} from directory {__PATH__}! "
                f"You have to create the file by your own. "
                f"You can use the tools in the project directory of EvolutionaryHuman or on GitHub: "
                f"https://github.com/AlbertUnruh/EvolutionaryHuman/tree/master/tools. "
                f"Context why you have to make this: to keep download-files small "
                f"you have to scrape the data by your own. But only have to do this once and not after every update."
            )

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
