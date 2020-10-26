
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


from service.check_in import CheckInService

from service.check_out import   CheckutService

from service.check_switch import CheckSwitchService
from service.repair_result import CheckRepairService
from service.outroot_subsidies import CheckoutrootService
from service.attendance import AttendanceService

application = Application([CheckInService,CheckutService,CheckSwitchService,CheckRepairService,
                           CheckoutrootService,AttendanceService],
                          'hs',
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
