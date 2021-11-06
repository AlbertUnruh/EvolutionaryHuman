def get_data(
    *,
    file: str,
    multiplier: int = 1000,
) -> tuple[list[int], list[int]]:
    """
    Parameters
    ----------
    file: str
    multiplier: int
        The multiplier for the counts.

    Returns
    -------
    tuple[list[int], list[int]]
        A tuple of ``ages`` and ``counts``.
    """
    raw_ages: str
    raw_counts: str
    # yes, I was really creative while naming the variables...
    semi_raw_ages: list[str]
    semi_raw_counts: list[str]
    ages: list[int]
    counts: list[int]

    with open(file) as f:
        raw_ages, raw_counts = f.read().splitlines()  # to remove the "\n"
    semi_raw_ages, semi_raw_counts = raw_ages.split(","), raw_counts.split(",")

    # fmt: off
    ages = [
        int(a.split("-")[0].removesuffix("+"))
        for a in semi_raw_ages
    ]
    counts = [
        int(a) * multiplier
        for a in semi_raw_counts
    ]
    # fmt: on

    return ages, counts


if __name__ == "__main__":

    class NoIdea(Exception):
        """just another exception..."""

    raise NoIdea(
        "\n"
        "I've no idea how to make things working in Python..\n"
        "I tried it in different ways but nothing worked for me...\n"
        "If you've an idea how to get a simple function (where I can use it as ``f(x)``) feel free to create a PR.\n"
        "\n"
        "I've come up by using my graphical calculator from school and came up with "
        "following function with logistical regression:\n"
        "6.38521E8/(1+0.006612*e^(0.08492*x))\n"
        "which leads to following code:\n"
        ">>> import math\n"
        ">>> def f(x):\n"
        "...     return 6.38521e8 / (1 + 0.006612 * math.e ** (0.08492 * x))\n"
        "\n"
        "Thanks\n"
        "~Albert"
    )
