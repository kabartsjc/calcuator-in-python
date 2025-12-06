import sys
import os

# Add project root to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import awm


def test_add_function_exists():
    assert hasattr(awm, "add")


def test_div_function_exists():
    assert hasattr(awm, "div")
