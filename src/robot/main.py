#-*-coding: utf-8 -*-
import sys, os

from twisted.internet import reactor
from twisted.application import service
from twisted.python import log
import time
from login import LoginRobot
from lobby import LobbyRobot
import redis,pickle

period     = 1# time diff
all        = 4# max robot num
users_per  = 2# start users_per robot per period
users_curr = 1# current robot num
lobby_users_curr = 1

application = service.Application('login test game Server')

    
def user_action(userid):
    username = "2000" + str(userid)
    # register
    r = LoginRobot(username)
    r.register(username)
    r.setServiceParent(service.IServiceCollection(application)) #@UndefinedVariable

def add_users():
    global users_curr, users_per, all
    if users_curr <= all:
        print users_curr
        for i in xrange(users_per):
            if users_curr <= all:
                reactor.callInThread(user_action, users_curr) #@UndefinedVariable
            users_curr += 1
        reactor.callLater(period, add_users) #@UndefinedVariable




reactor.callLater(1,add_users) #@UndefinedVariable


def ready_user_action(userid):
    username = "2000" + str(userid)
    r = LobbyRobot(username + "lobby")
    my = redis.StrictRedis(host='localhost', port=6379, db=0)
    print "username ======%s" % username
    user_obj = my.get(username)
    print user_obj
    user = pickle.loads(user_obj)
    r.ready(user.key)
    print "------------------user key --------------  %s" % user.key
    r.setServiceParent(service.IServiceCollection(application)) #@UndefinedVariable

def ready_user():
    print "--------enter ready user---------"
    global lobby_users_curr, users_per, all
    if lobby_users_curr <= all:
        print lobby_users_curr
        for i in xrange(users_per):
            if lobby_users_curr <= all:
                reactor.callInThread(ready_user_action, lobby_users_curr) #@UndefinedVariable
            lobby_users_curr += 1
        reactor.callLater(period, ready_user) #@UndefinedVariable


reactor.callLater(20, ready_user)



        
