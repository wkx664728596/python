from spyne import rpc,ServiceBase
from spyne import Unicode,String
import time

class AttendanceService(ServiceBase):
    @rpc(Unicode,Unicode,_returns=String)
    def sayhello(self,aa,bb):


        return 'hahahh'

    @rpc(Unicode, Unicode, _returns=String)
    def block(self,aa,bb):
        time.sleep(20)

        return 'block'



from wsgiref.simple_server import make_server

from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


application = Application([AttendanceService],
                          'hhahah',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    host = '0.0.0.0'
    port = 5001

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server(host, port, wsgi_application)
    server.serve_forever()
