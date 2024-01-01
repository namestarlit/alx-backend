#!/usr/bin/env python3
"""Simple pagination implementation"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a start and end indexes of a list"""
    # Compute the start index of the list
    start_index = (page - 1) * page_size

    # Compute the end index of the list
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Institantiates the Server class objects"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets data in a specified range of list indexes"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        # Get start and end index
        start_index, end_index = index_range(page, page_size)

        # Get data from the database cache
        data = self.dataset()

        # Check if index is out of range and return an empty list
        if start_index > len(data):
            return []

        return data[start_index:end_index]
