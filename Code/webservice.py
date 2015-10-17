from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
import os.path
import imp
from subprocess import Popen, PIPE, STDOUT,call 

def adder(a):
    if a == '1':
        if os.path.exists('/home/samara/Documentos/TG/TG-Background/Code/run_finger.py'):
            p = Popen(["python","/home/samara/Documentos/TG/TG-Background/Code/teste.py"], stdout=PIPE).communicate()[0]
            return p
        return 'NOT'
    return 'NOT'

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'result': str}, 
    args={'a': str})

print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
