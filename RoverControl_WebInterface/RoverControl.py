import cherrypy as cp
import render

cp.server.socket_host = '0.0.0.0'
cp.server.socket_port = 33480

class RoverControl(object):
  def index(self):
    return render.renderIndex()
  index.exposed = True

cp.quickstart(RoverControl())
