from requests import request
from os import fsync


def save_file(*, url: str, file: str) -> None:

    resp = request("GET", url, stream=True)
    resp.raise_for_status()

    with open(file, "wb") as f:
        for chunk in resp:
            if chunk:
                f.write(chunk)
                f.flush()
                fsync(f.fileno())


if __name__ == "__main__":
    save_file(
        url="https://raw.githubusercontent.com/organisciak/names/master/data/us-names-by-gender.csv",
        file="raw.csv",
    )
