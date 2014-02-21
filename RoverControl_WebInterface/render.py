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
  <input type="range" name="speed" id="spid" onchange="SpeedChanged(this)"/>
  <input type="range" name="steer" id="stid" onchange="SteeringChanged(this)"/>
  <div id="speed_out">Speed:</div>
  <div id="steer_out">Direction:</div>
  '''
  css = '''
  input[name="speed"] {
    position: absolute;
    -webkit-transform: rotate(270deg);
    top: 100px;
  }

  input[name="steer"] {
    margin-left: 300px;
    margin-top: 100px;
  }

  div[id="speed_out"] {
    margin-top: 150px;
  }

div[id="steer_out"] {
    margin-top: 10px;
  }

  '''
  js = ['main.js', 'jquery-2.1.0.min.js']
  return render(body=body, css=css, js=js)
