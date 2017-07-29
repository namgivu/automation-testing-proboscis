#region browser name
class Browser:
  Chrome  = 'Chrome'
  Firefox = 'Firefox'
  Android = 'Android'
  iOS     = 'iOS'

BROWSERS = [
  Browser.Chrome,

  #TODO more browser support here
  # Browser.Firefox,
  # Browser.Android,
  # Browser.iOS,
]
#endregion browser name


#basic path
import os ; APP_HOME = os.path.abspath(os.path.dirname(__file__))

###region snapshot setting
pass

#snapshot flag - TRUE/False means DO/don't take snapshot during the run
SNAPSHOT_DEBUG = False


##region snapshot folder
pass

#the snapshot home
SNAPSHOT_HOME = '%s/_snapshot_' % APP_HOME

#timestamp as 'YYYYmm-dd HHMMss ms' ref. https://stackoverflow.com/a/18406412/248616
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]

#prepare folder to store snapshot files for each run
SNAPSHOT_FOLDER = '{SNAPSHOT_HOME}/{timestamp}'.format(
  SNAPSHOT_HOME=SNAPSHOT_HOME, timestamp=timestamp,
)

pass
##endregion snapshot folder


pass
###endregion snapshot setting


#region enable all tests
"""ENABLED_TEST = True/False means all tests are enabled/disabled"""
ENABLED_TEST = True
#endregion


#region testing customer
TEST_CUSTOMER_GMAIL_ACCOUNT = 'aos.autotest.team'
TEST_CUSTOMER_EMAIL         = '%s@gmail.com' % TEST_CUSTOMER_GMAIL_ACCOUNT
TEST_CUSTOMER_PASS          = 'aos.autotest.team@gmail.com'
TEST_CUSTOMER_FULLNAME      = 'aos autotest team'
#endregion testing customer

#a valid order
TEST_ORDER_NUMBER = '64628'


#webdriver config i.e. to use local/remote webdriver
WEBDRIVER_REMOTE_HUB = '' #left empty to use local


#load local config
from config_local import * #local config is mandatory; please create one from
