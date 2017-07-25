"""
Testing for the math.py module.
"""

import fcm
import pytest

def test_add():
    assert fcm.math.add(4, 2973934) == 2973938
    assert fcm.math.add(0.12, 4) == 4.12
