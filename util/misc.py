#get current function name ref. https://stackoverflow.com/a/24628710/248616
import inspect
currentFuncName = lambda: inspect.stack()[1][3]


#wait for some seconds ref. https://stackoverflow.com/a/510351/248616
def wait(second=2):
  import time
  time.sleep(second)


#upload image given by a public URL to an upload input element in Selenium
def seleniumUploadFile(element, fileUrl):
  """selenium upload file/photo ref. https://stackoverflow.com/a/10472542/248616"""

  #generate temp file
  import tempfile
  downloadedFile = tempfile.NamedTemporaryFile() #ref. https://stackoverflow.com/a/13717435/248616
  downloadedFile = downloadedFile.name

  #download file from url
  import urllib
  urllib.urlretrieve(fileUrl, filename=downloadedFile) #ref. https://stackoverflow.com/a/22776/248616

  #do upload to element
  element.send_keys(downloadedFile)


#from gmail account, generate test email in the form of gmailAccount+timestamp@gmail.com
def generateTestEmail(gmailAccount):
  #timestamp as 'YYYYmm-dd HHMMss ms' ref. https://stackoverflow.com/a/18406412/248616
  from datetime import datetime
  timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]

  email = '%s+%s@gmail.com' % (gmailAccount, timestamp)
  return email

