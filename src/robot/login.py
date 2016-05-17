#-*-coding: utf-8 -*-

import sys, os
paths = ('.', '../')
import struct
for path in paths:
    _path = os.path.abspath(path)
    if _path not in sys.path: 
        sys.path.append(_path)

from robot.base import PbService, PbProtocol, PbFactory
import time
from twisted.internet import reactor, defer, protocol
from twisted.python import failure, log
from game.proto import login_pb2
import config

class LoginRobot(PbService):
    def __init__(self, name):
        self.name = name
        #self.Login(name)

    @defer.inlineCallbacks  
    def reg(self, name):
        log.msg('login request, name:%s '% name)
        try:
            LOGIN_connector = protocol.ClientCreator(reactor, PbProtocol )
            self.plogin = yield LOGIN_connector.connectTCP(config.ip, config.login_server_port)
            _factory = PbFactory(self)
            self.plogin.factory = _factory
        except Exception, e:
            self.plogin = None
            log.msg( 'Login... connect login error:', e ,self.name)
            reactor.callLater(10, self.Login, name)			
            defer.returnValue(None) 
        _msg = login_pb2.RegisterRequest()
        _msg.user_name = name
        _msg.password = "password"
        self.plogin.send(_msg)
    

     
    def regresponse(self, p, request):
        result = request.result
        token = request.token
        log.msg('loginresponse, result:%s, token:%s'% (result, token))



if __name__ == '__main__':
    aa = LoginRobot("s10009")
    aa = LoginRobot("s100010")
    aa = LoginRobot("s100011")
    reactor.run()
        
