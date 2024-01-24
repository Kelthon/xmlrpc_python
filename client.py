#!/usr/bin/python3

from random import randint
from xmlrpc import client

CONNECTION_IP = 'http://10.0.84.180'
CONNECTION_SOCKET = 21212

server = client.ServerProxy(f'{CONNECTION_IP}:{CONNECTION_SOCKET}')

print(server.system.listMethods())
print(server.getIP())
print(server.getDatetime())
print(server.addString(f'Hello Max{randint(1024, 2048)}'))
print(server.getString(0))
