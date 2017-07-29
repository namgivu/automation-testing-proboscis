"""
- Demo @test decorator at method level
- Note that we can make ANY method to be a test method; of course, that's not compatible with built-in python unittest
"""

from proboscis.asserts import assert_equal
from proboscis import test


@test(groups=["unit", "string"])
def test_reverse():
  """Make sure our complex string reversal logic works."""
  original = "hello"
  expected = "hello"
  actual = original
  assert_equal(expected, actual)
