import cherrypy
import logging
import render
import carcontrol
import traceback
import json
from utils.path import path

PATH_STATIC = path(__file__).parent.joinpath('static').abspath()
LOGFILE = path('.').joinpath('out.log')
app = None
log = logging.getLogger('rweb')

class RoverWeb(object):
  @cherrypy.expose
  def index(self):
    reload(render)
    return render.renderIndex()

  @cherrypy.expose
  def steerStraight(self):
    res = carcontrol.steerStraight()
    return json.dumps(res)

  @cherrypy.expose
  def steerLeft(self):
    res = carcontrol.steerLeft()
    return json.dumps(res)

  @cherrypy.expose
  def steerRight(self):
    res = carcontrol.steerRight()
    return json.dumps(res)

  @cherrypy.expose
  def driveStop(self):
    res = carcontrol.driveStop()
    return json.dumps(res)

  @cherrypy.expose
  def driveForward(self):
    res = carcontrol.driveForward()
    return json.dumps(res)
  
  @cherrypy.expose
  def driveBackward(self):
    res = carcontrol.driveBackward()
    return json.dumps(res)

def setupLogging():
  log.handlers = []
  log.setLevel(logging.DEBUG)

  sh = logging.StreamHandler()
  formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%m-%d %H:%M:%S")
  sh.setFormatter(formatter)
  log.addHandler(sh)

  logfile = LOGFILE
  log.info('storing logfile to %s' % logfile.normpath())

  fh = logging.FileHandler(logfile, 'a')
  fh.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s", '%m-%d %X'))
  log.addHandler(fh)
  logging.getLogger('cherrypy.error').addHandler(fh)

def handleError():
  '''cherrypy error handling function'''

  cherrypy.response.headers['Content-Type'] = 'text/plain'

  h = sorted("  %s: %s" % (k, v) for k, v in cherrypy.request.header_list)
  headers = '\nRequest Headers:\n' + '\n'.join(h)
  url = cherrypy.url(qs=cherrypy.request.query_string)

  formattedparams = ', '.join('%s: %s' %
    (k, v.encode('utf-8') if isinstance(v, basestring) else '?')
      for k, v in cherrypy.request.params.items())

  params = '\nRequest Parameters:\n  ' + (formattedparams if formattedparams.strip() else '<no parameters>')
  msg = '\nRequest Url:\n  %s\n%s\n %s\n\n' % (url, params, headers)

  log.error(msg, exc_info=True)

  stackTrace = "".join(traceback.format_exc())
  cherrypy.response.body = [''.join([msg, stackTrace, '\n'])]

def startServer(blocking=True):
  setupLogging()

  global app
  app = RoverWeb()

  globalconf = {
    'server.thread_pool'            : 50,
    'server.socket_host'            : '0.0.0.0',
    'server.socket_port'            : 33480,

    'engine.autoreload_on'          : False,
    'log.screen'                    : False,

    'tools.sessions.on'             : True,
    'tools.sessions.storage_type'   : 'ram',
    'checker.on'                    : False, # disable cherrypy checker
    'tools.decode.on'               : True, # decode with utf-8 - fallback to latin-1

    'tools.gzip.on'                 : True,
    'tools.gzip.compress_level'     : 6,
    #gzip these mimetypes
    'tools.gzip.mime_types'         : ['text/html', 'text/plain',
                                       'text/css', 'application/x-javascript',
                                       'text/javascript', 'text/xml', 'application/javascript',
                                       'application/json',],
    'tools.proxy.on'                : False,
    'tools.proxy.base'              : None,
    'tools.encode.on'               : True,
    'tools.encode.encoding'         : 'utf-8',
    'request.error_response'        : handleError,
  }

  cherrypy.config.update(globalconf)

  appconf = {}

  appconf['/static'] = {
   'tools.etags.on'         : True,
   'tools.etags.autotags'   : True,
   'tools.staticdir.on'     : True,
   'tools.staticdir.dir'    : PATH_STATIC,
   'tools.sessions.on'      : False,
  }

  cptree = cherrypy.tree.mount(app, '/', config = appconf )
  log.info('mounting server at %s:%s' % (globalconf['server.socket_host'], globalconf['server.socket_port']))
  cherrypy.engine.start()
  if blocking:
    cherrypy.engine.block()

def stopServer():
  cherrypy.engine.exit()

carcontrol.initGPIO()
startServer()
carcontrol.cleanupGPIO()
