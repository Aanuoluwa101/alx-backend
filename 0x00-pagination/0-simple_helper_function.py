#!/usr/bin/env python3


"""
Defines a function that returns a tuple of size two
containing a start index and an end index
corresponding to the range of indexes to return
in a list for some particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of size two
    containing a start index and an end index
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return start_index, end_index
