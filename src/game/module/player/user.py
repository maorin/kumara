#-*-coding: utf-8 -*-

import binascii
import os
from game.module.game.object.doll import Doll

class User(object):
    key = None
    dolls = []

    def __init__(self, username, password):
        self.user_name = username
        self.password = password
        
        if not self.key:
            self.key = self.generate_key()
    
    def __str__(self):
        return self.key
    
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()
        