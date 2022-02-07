#!/usr/bin/env python3
"""Pagination"""


def index_range(page=int, page_size=int)-> tuple:
    """helper funtion"""
    res = (page-1) * page_size
    return res, (res + page_size)
