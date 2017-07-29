from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from common import *


def wdw(driver, timeout=WebDriverWait_TIMEOUT):
  return WebDriverWait(driver, timeout)
