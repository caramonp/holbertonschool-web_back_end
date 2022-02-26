#!/usr/bin/env python3
"""
Auth module
"""
import hashlib


def _hash_password(password: str) -> str:
    """hash a password pass for user
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
