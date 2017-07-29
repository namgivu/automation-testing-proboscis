#import all test module
from test_vault import * #control which test to run in test_vault/__init__.py

##region print notable configured values

from util.common import *
from config import *

print('''
         HOME_PAGE_URL = {HL}{HOME_PAGE_URL}{EH}
  WEBDRIVER_REMOTE_HUB = {CM}{WEBDRIVER_REMOTE_HUB}{EH}
    TEST_VAULT_PACKAGE = {CM}{TEST_VAULT_PACKAGE}{EH}
        SNAPSHOT_DEBUG = {CM}{SNAPSHOT_DEBUG}{EH} {atSNAPSHOT_FOLDER}
''').format(
  HL=HL, CM=CM, EH=EH,
  HOME_PAGE_URL=HOME_PAGE_URL,
  WEBDRIVER_REMOTE_HUB=WEBDRIVER_REMOTE_HUB if WEBDRIVER_REMOTE_HUB else 'None i.e. use local webdriver',
  TEST_VAULT_PACKAGE=TEST_VAULT_PACKAGE,
  SNAPSHOT_DEBUG=SNAPSHOT_DEBUG,
  atSNAPSHOT_FOLDER='at %s' % SNAPSHOT_FOLDER if SNAPSHOT_DEBUG else '',
)

import sys ; sys.stdout.flush() #force to print right away ref. https://stackoverflow.com/a/26283838/248616

##endregion


#init Xvfb ref. https://stackoverflow.com/a/30103931/248616
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start() #TODO ensure if we need to call display.close()

#prepare snapshot folder if debug snapshot required
if SNAPSHOT_DEBUG:
  import os ; os.makedirs(SNAPSHOT_FOLDER)  #create folder path recursively ref. https://stackoverflow.com/a/41146954/248616

#run test via proboscis
from proboscis import TestProgram
TestProgram().run_and_exit()
