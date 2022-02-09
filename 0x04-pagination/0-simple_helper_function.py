#!/usr/bin/env python3
"""Pagination"""


def index_range(page=int, page_size=int)-> tuple:
    """helper funtion"""
    return (((page - 1) * page_size), (page * page_size))
