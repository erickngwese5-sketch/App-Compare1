import numpy as np
import sys
from pathlib import Path

# Ensure the repository root is on the Python path so that App.py can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from App import parse_dimension


def test_parse_dimension_lowercase():
    assert parse_dimension('3 x 5') == (3.0, 5.0)


def test_parse_dimension_uppercase():
    assert parse_dimension('3 X 5') == (3.0, 5.0)


def test_parse_dimension_multiplication_sign():
    assert parse_dimension('3×5') == (3.0, 5.0)


def test_parse_dimension_invalid():
    w, h = parse_dimension('invalid')
    assert np.isnan(w) and np.isnan(h)
