"""ref. https://getbootstrap.com/css/#grid-options"""
"""ref. Chrome inspector @ view with device mode ref. https://developers.google.com/web/tools/chrome-devtools/device-mode"""
"""width x height"""


class WindowSize:

  #maximized
  MAXIMIZED = 'MAXIMIZED'

  #desktop
  PC_width  = 1200
  PC_height = 800
  PC = '%sx%s' % (PC_width, PC_height)
  PC_dict = dict(width=PC_width, height=PC_height)

  #mobile
  MB_width  = 360
  MB_height = 640
  MB = '%sx%s' % (MB_width, MB_height)
  MB_dict = dict(width=MB_width, height=MB_height)
