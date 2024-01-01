#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of pupular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Instantiates an instance of the Server class"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]

            # Index dataset with numbers
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns metadata and data from a given index and page size"""
        # Get the indexed data
        data = self.indexed_dataset()

        # Assert that the index is valid
        assert index is not None and index >= 0
        assert index <= max(data.keys())

        page_data = []
        data_count = 0
        next_index = None
        start_index = index if index else 0

        # Append data in the page_data list
        for key, value in data.items():
            if key >= start_index and data_count < page_size:
                page_data.append(value)
                data_count += 1
                continue

            if data_count == page_size:
                next_index = key
                break

        # Construct page metadata info
        page_info = {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }

        return page_info
