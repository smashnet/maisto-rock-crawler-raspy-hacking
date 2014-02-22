from collections import defaultdict

BASE = '''
<html>
  <head>
    %(js)s
    %(css)s
    <style type="text/css">
      a {color: #0000e0;}
    </style>
  </head>
  <body>
    %(body)s
  </body>
</html>
'''

def render(body=None, js=None, css=None):
  # prepare js definitions - optionally add a file given by @param js
  js_line = '<script type="text/javascript" src="/static/js/%s">&#160;</script>'
  css_line = '<link href="/static/css/%s" type="text/css" rel="stylesheet">'

  jsdefs = [js_line % f for f in js]
  cssdefs = [css_line % f for f in css]
  data = {}
  data['body'] = body
  data['js'] = '\n\t'.join(jsdefs)
  data['css'] = '\n\t'.join(cssdefs)
  return BASE % data

def renderIndex():
  body = '''
  <div class="container">
    <div class="page-header">
      <h1>Rover Control <small>Web Interface</small></h1>
    </div>
    <div class="row">
      <div class="col-sm-1">
        <button type="button" class="btn btn-default btn-lg" onMouseDown="PushedForward(this);" onMouseUp="ReleasedForward(this);">
          <span class="glyphicon glyphicon-arrow-up"></span>
        </button><br/>
        <button type="button" class="btn btn-default btn-lg" onMouseDown="PushedBackward(this);" onMouseUp="ReleasedBackward(this);">
          <span class="glyphicon glyphicon-arrow-down"></span>
        </button>
      </div>
      <div class="col-sm-10">
        <a href="#" class="thumbnail">
          <img data-src="holder.js/800x533" alt="Rover camera stream">
        </a>
      </div>
      <div class="col-sm-1">
        <button type="button" class="btn btn-default btn-lg" onclick="ToggleRight(this);">
          <span class="glyphicon glyphicon-arrow-right"></span>
        </button><br/>
        <button type="button" class="btn btn-default btn-lg" onclick="ToggleLeft(this);">
          <span class="glyphicon glyphicon-arrow-left"></span>
        </button>
      </div>
    </div>
  </div>
  '''
  css = ['bootstrap.min.css', 'main.css']
  js = ['jquery-2.1.0.min.js', 'bootstrap.min.js', 'holder.js', 'main.js']
  return render(body=body, css=css, js=js)
