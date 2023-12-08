"""Function practice."""


def merge_lists(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Combines a str list and a int list into a dict."""
    result: dict[str, int] = {}
    i: int = 0
    if len(str_list) != len(int_list):
        return result
    for string in str_list:
        result[string] = int_list[i]
        i += 1
    return result

print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))