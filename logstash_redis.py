#!/bin/python

import redis

class CRedis:

    def __init__(self, host="localhost", port=6379,db=0, channel="loghstash"):
        ''' define the productor '''
        self.host = host
        self.port = port
        self.db = db
        self.channel = channel
        self.conn = redis.Redis(self.host, self.port)

    def setChannel()