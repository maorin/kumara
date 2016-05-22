import sys
_path = ('..')
if _path not in sys.path:
    sys.path.append(_path)
from protocol.lobby  import LobbyService
from twisted.python import log
from game.proto import lobby_pb2
from twisted.internet import defer
import random

class LobbyServer(LobbyService):
    
    #@defer.inlineCallbacks
    def readyrequest(self, p, request):
        token = request.token
        log.msg("readyrequest", token)
        log.msg("---------%s", self.ids)
        
        
        if self.ids:
            opp_id = random.choice(self.ids)
            self.ids.remove(opp_id)
            opp_p = p.factory.connmanager.getConnectionByID(opp_id)
            _msg = lobby_pb2.EnterBattleResponse()
            _msg.channel = "111111110010"
            log.msg("--------opp_p-----%s", opp_p)
            p.send(_msg)
            opp_p.send(_msg)
            
        else:        
            self.ids.append(p.transport.sessionno)
            _msg = lobby_pb2.ReadyResponse()
            _msg.result = "1"
            log.msg("------%s---connmanger---- listcount:%s----- " % (token, p.factory.connmanager.getNowConnCnt()))
            p.send(_msg)
        
        
        
        '''
        for conn_key in p.factory.connmanager.getConnList().keys():
            log.msg("------send-----connkey %s" % p.factory.connmanager.getConnList()[conn_key])
            _msg = lobby_pb2.EnterBattleResponse()
            _msg.channel = "111111110010"
            p.factory.connmanager.getConnList()[conn_key].send(_msg)
        '''
        
        
        