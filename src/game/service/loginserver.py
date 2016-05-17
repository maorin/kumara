#-*-coding: utf-8 -*-

import sys
_path = ('..')
if _path not in sys.path:
    sys.path.append(_path)
from game.protocol.login import LoginService
from twisted.python import log
from game.proto import login_pb2
import txredisapi as redis

from twisted.internet import defer
from twisted.internet import reactor




class LoginService(LoginService):

    def registerrequest(self, p, request):
        user_name = request.user_name
        
        
        _msg = login_pb2.RegisterResponse()
        _result = '1'
        _msg.result = _result
        _msg.user_name = "register been...." + user_name					
        p.send(_msg)
    
    """
    @summary: 目前使用用户名就可以登录，如果没有用户直接创建这个用户，直接可以进入大厅
    用户token 用户名 +  123
    """
    @defer.inlineCallbacks    
    def loginrequest(self, p, request):
        user_name = request.user_name
        rc = yield redis.ConnectionPool()
        v = yield rc.get(user_name)
        if not v:
            yield rc.set(user_name, user_name+"123")
        
        v = yield rc.get(user_name)
        print "foo:", repr(v)
        log.msg("------------foo::::::::-----------", repr(v))
        yield rc.disconnect()
        
        _msg = login_pb2.LoginResponse()
        _result = '1'
        _msg.result = _result
        _msg.user_name = user_name					
        p.send(_msg)
    

