#!/usr/bin/env python3


"""Defines a function that returns the
   appropriate page of a dataset"""


import csv
import math
from typing import List, Tuple, Union, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two
    containing a start index and an end index
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of the dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()

        try:
            # get the index to start and end at
            start, end = index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[List]]]:
        """Returns a dictionary"""
        dataset = self.dataset()
        next_page = page + 1 if index_range(page, page_size)[1] \
            < len(dataset) - 1 else None
        prev_page = page - 1 if page > 1 else None
        data = self.get_page(page, page_size)
        calculated_page_size = len(data)

        return {'page_size': calculated_page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': math.ceil(len(dataset) / page_size)
                }
