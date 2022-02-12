#!/usr/bin/env python3
"""Personal Data- Log formatter
"""

import hashlib
import bcrypt


def hash_password(password: str) -> bytes:
    """ function that expects password and returns a salted
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(str.encode(password), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check valid password
    """
    return bcrypt.checkpw(password, hashed_password)
