#
# Copyright (c) 2023 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
"""This module implements some keywords for use by Robot Framework."""

def sum_as_string(first_number: int, second_number: int) -> str:
    """Keyword to return the sum of two integers as string."""
    return str(first_number + second_number)

def join_strings(string_list: list[str]) -> str:
    """Keyword to return the comma separated list of strings."""
    return ",".join(string_list)

def sum_values(values_dict: dict[str, int]) -> int:
    """Keyword to return the sum of the values for all keys in the dictionary."""
    values_sum: int = 0
    for _, value in values_dict.items():
        values_sum += value
    return values_sum
