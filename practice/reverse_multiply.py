"""Function practice."""


def reverse_multiply(nums: list[int]) -> list[int]:
    result: list[int] = [0] * len(nums)
    i: int = 1
    for num in nums:
        num *= 2
        result[len(nums) - i] = num
        i+= 1
    return result

print(reverse_multiply([1, 2, 3]))