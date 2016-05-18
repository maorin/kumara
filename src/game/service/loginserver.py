#-*-coding: utf-8 -*-

import sys
_path = ('..')
if _path not in sys.path:
    sys.path.append(_path)
from protocol.login import LoginService
from twisted.python import log
from game.proto import login_pb2
import txredisapi as redis

from twisted.internet import defer
from twisted.internet import reactor
import pickle
from game.module.player.user import User

class LoginServer(LoginService):
    
    @defer.inlineCallbacks  
    def registerrequest(self, p, request):
        log.msg("-----------enter this--")
        username = request.user_name
        password = request.password
        
        _msg = login_pb2.RegisterResponse()
        rc = yield redis.Connection()
        v = yield rc.get(username)
        log.msg("-----vvvvvvvvvvvvvvv------", v)
        if v:
            _msg.result = "0"
            _msg.token = "register been...."					
        else:
            log.msg("-----------enter this--")
            user = User(username, password)
            pickled_user = pickle.dumps(user)
            yield rc.set(username, pickled_user)
            yield rc.set(user.key, pickled_user)
            log.msg("create user: %s  and key: %s", username, user.key)
            _msg.result = "1"
            _msg.token = user.key
        yield rc.disconnect()
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
    

