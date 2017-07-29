"""
- Demo @test decorator with mixed class-method
  ref. http://pythonhosted.org/proboscis/#using-testng-style-test-methods-to-factor-out-global-variables

> Run test methods in the style of TestNG by putting the @test decorator on both the class
  and test methods and making sure the class does NOT extend unittest.TestCase

"""

from proboscis import test


@test(groups=["unit", "number"])
class TestIsNegative(object):

  @test(groups=["service.initialization"])
  def service_initialize(self):
    """service_initialize"""

  @test(groups=["user", "user.initialization"],
        depends_on_groups=["service.initialization"])
  def create_user(self):
    """Create new user"""
    #assert_true(1+1==22) #NOTE: If this one is turned on, its dependant e.g. group 'user.test' won't run

  @test(groups=["user", "user.test"],
        depends_on_groups=["user.initialization"])
  def a_failOnPurpose_dummy(self):
    """a_failOnPurpose_dummy"""
    from proboscis.asserts import assert_true
    assert_true(1 + 1 == 333)

  @test(groups=["service.shutdown"],
        depends_on_groups=["user.test"],
        always_run=True)
  def shut_down(self):
    """Shut down service"""
