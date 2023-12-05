"""Dictionary related utility functions."""

__author__ = "730671130"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element of the list
    for elem in table:
        # for each dictionary, get the value at key "header" and add to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column vals
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        first_n_values: list[str] = []
        for i in range(num_rows):
            if i < len(table[column]):
                first_n_values.append(table[column][i])
        result[column] = first_n_values
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces column-based table with specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = table[column]
    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first_table:
        result[column] = first_table[column]
    for column in second_table:
        if column in result:
            result[column] += second_table[column]
        else:
            result[column] = second_table[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produces dict with keys being unique values in given list and values being the number of times it appears."""
    result: dict[str, int] = {}
    for num in values:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result