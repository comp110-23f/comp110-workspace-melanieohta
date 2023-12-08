"""Function practice."""


def multiples(num_list: list[int]) -> list[bool]:
    """Tells whether each int is a multiple of the previous value."""
    result: list[bool] = []
    if num_list[0] % num_list[len(num_list) - 1] == 0:
        result.append(True)
    else:
        result.append(False)
    i: int = 1
    while i < len(num_list):
        if num_list[i] % num_list[i - 1] == 0:
            result.append(True)
        else:
            result.append(False)
        i += 1
    return result