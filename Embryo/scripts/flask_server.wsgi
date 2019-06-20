import os
import logging, sys
logging.basicConfig(stream=sys.stderr)
PROJECT_DIR = '/home/pi/Embryo/scripts/'
sys.path.insert(0, PROJECT_DIR)
def execfile(filename):
    globals = dict( __file__ = filename )
    exec( open(filename).read(), globals )


activate_this = os.path.join( PROJECT_DIR , 'py3/bin', 'activate_this.py' )
#execfile( activate_this )
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

#if sys.version_info[0]<3:       # require python3
# raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

#sys.path.insert(0, '/home/pi/Embryo/scripts/')
from server_main  import app as application
application.debug = True

