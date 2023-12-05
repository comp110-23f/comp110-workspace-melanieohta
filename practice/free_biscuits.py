"""Practice free_biscuits function."""

def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
    """My doc string."""
    result: dict[str, bool] = {}
    # loop over each key in input dictionary
    for key in input:
        # for each element of the dictionary, sum up its values
        list_to_sum: list[int] = input[key]
        sum: int = 0
        # loop through list and add each value to sum
        for element in list_to_sum:
            sum += element
        # if sum >= 100, store in result under key "key" with value True
        if sum >= 100:
            result[key] = True
        else: # if not store as False
            result[key] = False
    return result

test: dict[str, list[int]] = {"UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23]}
free_biscuits(test)