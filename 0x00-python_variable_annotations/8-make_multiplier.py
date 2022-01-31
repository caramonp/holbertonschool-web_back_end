#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns multiply function"""
    def multiply(number: float) -> float:
        return multiplier * number
    return multiply
