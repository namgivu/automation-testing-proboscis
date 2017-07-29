"""
- Demo @test decorator to define group dependency relationship
"""

from proboscis.asserts import assert_true
from proboscis import test


@test(groups=["service.initialization"])
def service_initialize():
  """service_initialize"""


@test(groups=["user", "user.initialization"],
      depends_on_groups=["service.initialization"])
def create_user():
  """Create new user"""
  #assert_true(1+1==22) #NOTE: If this one is turned on, its dependant e.g. group 'user.test' won't run


@test(groups=["user", "user.test"],
      depends_on_groups=["user.initialization"])
def a_failOnPurpose_dummy():
  """a_failOnPurpose_dummy"""
  from proboscis.asserts import assert_true
  assert_true(1+1==333)


@test(groups=["service.shutdown"],
      depends_on_groups=["user.test"],
      always_run=True)
def shut_down():
  """Shut down service"""
