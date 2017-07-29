#region import test vault
import importlib
from config import TEST_VAULT_PACKAGE

for pkg in TEST_VAULT_PACKAGE:
  #import via string variable ref. https://stackoverflow.com/a/14000967/248616
  im = importlib.import_module('test_vault.%s' % pkg)

  #import * from the package ref. https://stackoverflow.com/q/44492803/248616
  importAll = im.__dict__
  globals().update(importAll)

#endregion import test vault
