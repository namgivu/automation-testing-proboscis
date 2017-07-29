from proboscis import test
from config import *
from util import *


@test(enabled=True)
def test_alert_box():
  """Test alert box"""

  ##region prepare the html file
  html='''
<!DOCTYPE html>
<html>
<body>

<p>Click the button to display an alert box.</p>

<button onclick="myFunction()">Try it</button>
<input id='myTextbox'>

<script>
function myFunction() {
  alert("Hello! I am an alert box!");
}
</script>

</body>
</html>
  '''

  #generate temp file
  import tempfile
  htmlFile = tempfile.NamedTemporaryFile().name #ref. https://stackoverflow.com/a/13717435/248616

  #write html to file ref. https://stackoverflow.com/a/27708256/248616
  with open(htmlFile, 'w') as f:
    f.write(html)
  ##endregion prepare the html file

  #open sample alert page
  driver = loadWebDriver(WEBDRIVER_REMOTE_HUB, WindowSize.PC)
  driver.get('file:///'+htmlFile)
  wait()  #must wait here to ensure below code work
  takeSnapshot(driver, prefix=currentFuncName(), suffix='1st-load')

  myTextbox = driver.find_element_by_css_selector('input#myTextbox')
  myTextbox.send_keys('abbccc')
  takeSnapshot(driver, prefix=currentFuncName(), suffix='try-textbox')


  #click 'Try it'
  #<button onclick="myFunction()">Try it</button>

  tryIt = driver.find_element_by_xpath("//button[text()='Try it']")
  tryIt.click()

  alertBox = driver.switch_to_alert()
  # alertBox = wdw(driver).until(EC.alert_is_present()) #TODO Why alert box not available?

  takeSnapshot(driver, prefix=currentFuncName(), suffix='try-alert')




