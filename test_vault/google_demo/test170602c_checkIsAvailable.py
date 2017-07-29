from proboscis import test
from pom.google_demo.chrome import POM_aos_web_CHROME as pom
from config import ENABLED_TEST


@test(groups=['G00.checkIsAvailable', 'chrome'], enabled=ENABLED_TEST)
def test_urlStatus200():
  """Check web homepage at url - should be status 200"""
  pom.testIsAvailable_via_urlStatus200()


@test(groups=['G00.checkIsAvailable', 'chrome'], depends_on=[test_urlStatus200], enabled=ENABLED_TEST)
def test_onPCScreen():
  """Check web homepage with pc screen"""
  pom.testIsAvailable_onPCScreen()


@test(groups=['G00.checkIsAvailable', 'chrome'], depends_on=[test_urlStatus200, test_onPCScreen], enabled=ENABLED_TEST)
def test_on_MB_screen():
  """Check web homepage with mobile screen"""
  pom.testIsAvailable_on_MB_screen()
