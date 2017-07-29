HOME_PAGE_URL='YOUR_HOME_PAGE_URL'
HOME_PAGE_TITLE='YOUR_HOME_PAGE_TITLE'

#list of test vault packages to run
"""Comment on/off below lines to add/omit test in the corresponding package"""
TEST_VAULT_PACKAGE=[
  'YOUR_TEST_PACKAGE1',
  'YOUR_TEST_PACKAGE2',
]


#region SNAPSHOT_DEBUG=TRUE/False means DO/don't take snapshot during the run
# SNAPSHOT_DEBUG = True
#endregion


#region ENABLED_TEST=TRUE/False means DO/don't enable all tests
# ENABLED_TEST = False
#endregion


#region webdriver config i.e. to use local/remote webdriver
pass

# WEBDRIVER_REMOTE_HUB = '' #left empty to use local
WEBDRIVER_REMOTE_HUB = 'http://localhost:4444/wd/hub' #4444 the hub-node grid
# WEBDRIVER_REMOTE_HUB = 'http://localhost:4445/wd/hub' #4445 the standalone chrome hub
# WEBDRIVER_REMOTE_HUB = 'http://localhost:4446/wd/hub' #4446 the standalone firefox hub

pass
#endregion