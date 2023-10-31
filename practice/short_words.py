"""Short words practice function."""

__author__ = "730671130"


def short_words(list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for word in list:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list