import sys
_path = ('..')
if _path not in sys.path:
    sys.path.append(_path)
from protocol.lobby  import LobbyService
from twisted.python import log
from game.proto import lobby_pb2

class LobbyServer(LobbyService):

    def readyrequest(self, p, request):
        user_name = request.user_name
        log.msg("loginrequest", user_name)

        _msg = lobby_pb2.ReadyResponse()
        _result = '0' if user_name else '1'	
        _msg.result = _result
        _msg.user_name = "ddddddddddddddddddd" + user_name					
        p.send(_msg)