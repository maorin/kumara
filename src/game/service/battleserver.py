#-*-coding: utf-8 -*-


import sys
_path = ('..')
if _path not in sys.path:
    sys.path.append(_path)
from protocol.battle import BattleService
from twisted.python import log
from game.proto import battle_pb2

class BattleServer(BattleService):
    #命令卡牌出战   
    def gorequest(self, p, request):
        user_name = request.user_name
        log.msg("create_solder——request", user_name)

        _msg = battle_pb2.goResponse()
        _msg.result = '1'
        _msg.user_name = "222222222222222999999999999999999999" + user_name                  
        p.send(_msg)
    
        
    def enterbattlerequest(self, p, request):
        #TODO
        #
        pass