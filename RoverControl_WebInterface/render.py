from collections import defaultdict

BASE = '''
<html>
  <head>
    %(js)s
    <style type="text/css">
      a {color: #0000e0;}
    </style>
    <style type="text/css">
      %(css)s
    </style>
  </head>
  <body style="font-family: arial;">
    %(body)s
  </body>
</html>
'''

def render(js=None, **kwargs):
  # prepare js definitions - optionally add a file given by @param js
  s = '<script type="text/javascript" src="/static/%s">&#160;</script>'
  jsfiles = []
  if isinstance(js, basestring):
    jsfiles.append(js)
  elif isinstance(js, (list, tuple)):
    jsfiles.extend(js)

  jsdefs = [s % f for f in  jsfiles]
  data = defaultdict(str)
  data.update(kwargs)
  data['js'] = '\n        '.join(jsdefs)
  return BASE % data

def renderIndex():
  body = '''
  Welcome to Rover Control 1.0!<br/><br/>
  <video id="video" src="rtp://raspberrypi:1234" autoplay="autoplay" />
  '''
  return render(body=body)
