#-*-coding: utf-8 -*-

import sys, os

paths = ('.', '../')

for path in paths:
    _path = os.path.abspath(path)
    if _path not in sys.path:
        sys.path.append(_path)

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

from twisted.internet import reactor
reactor.suggestThreadPoolSize(50)

from twisted.application import internet, service
from game.service.loginserver import LoginService
from game.service.lobbyserver import LobbyService
from game.service.battleserver import BattleService
import config
from game.base import PbFactory


loubiService = service.MultiService()


login_server = LoginService()
#login_server.setServiceParent(service.IServiceCollection(application)) #@UndefinedVariable
_login_factory = PbFactory(login_server)
internet.TCPServer(config.login_server_port, _login_factory).setServiceParent(loubiService)

lobby_server = LobbyService()
_lobby_factory = PbFactory(lobby_server)
internet.TCPServer(config.lobby_server_port, _lobby_factory).setServiceParent(loubiService)

battle_server = BattleService()
_battle_factory = PbFactory(battle_server)
internet.TCPServer(config.battle_server_port, _battle_factory).setServiceParent(loubiService)

application = service.Application('MaoJ loubi Server')
loubiService.setServiceParent(application)

