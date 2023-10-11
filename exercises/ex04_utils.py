"""Implementing algorithms by working with lists and their built in methods."""
__author__ = "730671130"

def all(num_list: list[int], num: int) -> bool:
    i: int = 0
    count: int = 0
    while i < len(num_list):
        if num_list[i] == num:
            count += 1
    if count == len(num_list):
        return True
    return False

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_int: int = input[0]
    i: int = 1
    while i < len(input):
        if input[i] > max_int:
            max_int = input[i]
    return max_int

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if(len(list1) != len(list2)):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
    return True