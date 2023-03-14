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
