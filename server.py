#!/usr/bin/python3

from datetime import datetime
from xmlrpc import server
from typing import List

SERVER_IP = 'http://10.0.84.180'
SERVER_SOCKET = 21212
strlist: List[str] = []

class RequestHandler(server.SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with server.SimpleXMLRPCServer(('10.0.84.180', SERVER_SOCKET), requestHandler=RequestHandler) as rpc_server:
    rpc_server.register_introspection_functions()

    def getIP():
        return SERVER_IP

    def getDatetime():
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def addString(string: str):
        strlist.append(string)
        return "success"

    def getString(index: int):
        return strlist[index]

    rpc_server.register_function(getIP, 'getIP')
    rpc_server.register_function(getDatetime, 'getDatetime')
    rpc_server.register_function(addString, 'addString')
    rpc_server.register_function(getString, 'getString')

    rpc_server.serve_forever()
