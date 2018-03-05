#!/usr/bin/env python3
import argon2
import os
if __name__ == "__main__":
    from _utils import SALT_SIZE, bytes_to_hex
else:
    from ._utils import SALT_SIZE, bytes_to_hex


"""
Docs:
    - https://github.com/P-H-C/phc-winner-argon2
    - http://argon2-cffi.readthedocs.io/en/stable/api.html#argon2.low_level.hash_secret
"""
def get_hash(password, salt):
    password_hash = argon2.low_level.hash_secret(
        password.encode(),
        salt.encode(),
        time_cost=10,
        memory_cost=32*1024,
        parallelism=1,
        hash_len=128,
        type=argon2.low_level.Type.ID
    )
    return password_hash.decode()


def get_salt():
    return bytes_to_hex(os.urandom(SALT_SIZE))


"""
Why salt isn't needed?
    - https://github.com/P-H-C/phc-string-format/blob/master/phc-sf-spec.md

Docs:
    - http://argon2-cffi.readthedocs.io/en/stable/api.html#argon2.low_level.verify_secret
"""
def compare_hash(hash, password):
    try:
        return argon2.low_level.verify_secret(hash.encode(), password.encode(), argon2.low_level.Type.ID)
    except argon2.exceptions.VerifyMismatchError:
        return False
    except argon2.exceptions.VerificationError:
        return False


def _test_hash():
    salt = get_salt()
    password = "pass"
    hash = get_hash(password, salt)
    assert compare_hash(hash, password)


if __name__ == "__main__":
    _test_hash()