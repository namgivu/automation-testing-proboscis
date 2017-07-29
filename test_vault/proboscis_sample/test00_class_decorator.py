"""
- Demo @test decorator at class level
- Note that we create test class and test method the same way with built-in python-unittest framework
"""

import unittest
from proboscis import test


@test(groups=["unit", "number"])
class TestIsNegative(unittest.TestCase):
  """Confirm that utils.is_negative works correctly."""

  def test_should_return_true_for_negative_numbers(self):
    self.assertTrue(-47<0)

  def test_should_return_false_for_positive_numbers(self):
    self.assertFalse(56<0)

  def test_should_return_false_for_zero(self):
    self.assertFalse(0<0)
