#-*-coding: utf-8 -*-

import sys, os
paths = ('.', '../')
import struct
for path in paths:
    _path = os.path.abspath(path)
    if _path not in sys.path: 
        sys.path.append(_path)

from protocol.lobby import LobbyService, LobbyProtocol, LobbyFactory
import time
from twisted.internet import reactor, defer, protocol
from twisted.python import failure, log
from game.proto import lobby_pb2
import config

class LobbyRobot(LobbyService):
    def __init__(self, name):
        self.name = name
        #self.Login(name)

    @defer.inlineCallbacks  
    def ready(self, token):
        log.msg('login request, token:%s '% token)
        try:
            LOBBY_connector = protocol.ClientCreator(reactor, LobbyProtocol )
            self.plogin = yield LOBBY_connector.connectTCP(config.ip, config.lobby_server_port)
            _factory = LobbyFactory(self)
            self.plogin.factory = _factory
        except Exception, e:
            self.plogin = None
            log.msg( 'Login... connect login error:', e ,self.name)
            reactor.callLater(10, self.ready, token)			
            defer.returnValue(None) 
        _msg = lobby_pb2.ReadyRequest()
        _msg.token = token
        self.plogin.send(_msg)
    

    
    def readyresponse(self, p, request):
        result = request.result
        log.msg('registerresponse, result:%s'% (result))
    


if __name__ == '__main__':
    aa = LobbyRobot("s10009")
    aa.ready("s10009")
    reactor.run()
        
