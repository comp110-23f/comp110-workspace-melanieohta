"""Function practice."""


def max_key(dict: dict[str, list[int]]) -> str:
    """Returns key with highest sum of values."""
    max_sum: int = 0
    max_str: str = ""
    for key in dict:
        sum: int = 0
        for num in dict[key]:
            sum += num
        if sum > max_sum:
            max_sum = sum
            max_str = key
    return max_str

print(max_key({"a": [1,2,3], "b": [4,5,6]}))