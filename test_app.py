import pytest
from app import calculate_total


def test_calculate_total_basic():
  assert calculate_total(10.0, 3) == 30.0


def test_calculate_total_with_discount():
  assert calculate_total(100.0, 2, 10) == 180.0


def test_calculate_total_no_discount():
  assert calculate_total(50.0, 2, 0) == 100.0


def test_calculate_total_negative_values():
  with pytest.raises(ValueError):
    calculate_total(-5.0, 2, 10)
