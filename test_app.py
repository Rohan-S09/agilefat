import pytest
from app import calculate_total


def test_calculate_total_basic():
  assert calculate_total(10.0, 3) == 30.0


def test_calculate_total_zero():
  assert calculate_total(5.0, 0) == 0.0


def test_calculate_total_negative():
  try:
    calculate_total(-5.0, 2)
    assert False, "Expected ValueError"
  except ValueError:
    assert True
