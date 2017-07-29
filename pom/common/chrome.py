from proboscis.asserts import assert_equal

from config import *
from util import *


class POM_common_CHROME:

  def __init__(self): pass


  ##region checkIsAvailable
  pass


  @staticmethod
  def testIsAvailable_via_urlStatus200():
    """Check web homepage at url - should be status 200"""
    #TODO Caution for case that page is redirect and status to be 302 ref. https://stackoverflow.com/a/2839594/248616
    import requests
    r = requests.get(HOME_PAGE_URL)
    assert_equal(actual=r.status_code, expected=200)


  @staticmethod
  def testIsAvailable_onPCScreen():
    """Check web homepage with pc screen"""
    try:
      driver = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)
      driver.get(HOME_PAGE_URL)
      assert_equal(actual=driver.title, expected=HOME_PAGE_TITLE)

    finally:
      driver.quit()



  @staticmethod
  def testIsAvailable_on_MB_screen():
    """Check web homepage with mobile screen"""
    try:
      driver = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.MB)
      driver.get(HOME_PAGE_URL)
      assert_equal(actual=driver.title, expected=HOME_PAGE_TITLE)

    finally:
      driver.quit()


  pass
  ##endregion checkIsAvailable
