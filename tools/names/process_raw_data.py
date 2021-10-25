def get_file_content(*, file: str) -> str:
    with open(file) as f:
        return f.read()


def save_file(*, content: str, file: str) -> None:
    with open(file, "w") as f:
        f.write(content)


def extract_gender(*, sex: str, csv: str) -> set[str]:
    found = set()
    for line in csv.splitlines():
        _sex, _name, _count = line.split(",")
        if sex == _sex:
            found.add(_name)
    return found


def extract_male(*, csv: str) -> set[str]:
    return extract_gender(sex="M", csv=csv)


def extract_female(*, csv: str) -> set[str]:
    return extract_gender(sex="F", csv=csv)


def set_to_txt(*, set_to_convert: set[str]) -> str:
    return "\n".join(set_to_convert)


if __name__ == "__main__":
    all_names = get_file_content(file="raw.csv")

    male = extract_male(csv=all_names)
    female = extract_female(csv=all_names)

    del all_names

    neutral = set()
    for n in male:
        if n in female:
            neutral.add(n)

    save_file(file="male.txt", content=set_to_txt(set_to_convert=male))
    save_file(file="female.txt", content=set_to_txt(set_to_convert=female))
    save_file(file="neutral.txt", content=set_to_txt(set_to_convert=neutral))
