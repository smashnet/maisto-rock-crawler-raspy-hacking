import cherrypy as cp

cp.server.socket_host = '0.0.0.0'
cp.server.socket_port = 33480

class RoverControl(object):
  def index(self):
    return "Welcome to Rover Control 1.0!"
  index.exposed = True

cp.quickstart(RoverControl())
