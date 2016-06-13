#!/bin/python

import redis

class CRedis:

    def __init__(self, host="localhost", port=6379,db=0):
        ''' define the productor '''
        self.host = host
        self.port = port
        self.db = db
        self.channel = channel
        self.conn = redis.Redis(self.host, self.port)

    def setChannel(self, channel):
        ''' Set the publish channel '''
        self.channel = channel
        return self 

    def publishMsg(self, message):
        '''publish the message'''
