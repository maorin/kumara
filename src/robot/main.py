#-*-coding: utf-8 -*-
import sys, os

from twisted.internet import reactor
from twisted.application import service
from twisted.python import log
import time
from login import LoginRobot

period     = 1# time diff
all        = 100# max robot num
users_per  = 5# start users_per robot per period
users_curr = 1# current robot num

application = service.Application('robot test game Server')

    
def user_action(userid):
    r = LoginRobot("s%s" % ("2000" + str(userid)))
    r.register("s%s" % ("2000" + str(userid)))
    #r.goloubi("s%s" % ("1000" + str(userid)))
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



        
