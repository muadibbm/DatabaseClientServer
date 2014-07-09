'''
Created on 2014-07-09

@author: Mehrdad Dehdashti
'''

import socket

class Server(object):
    '''
    Server Class
    '''

    def __init__(self, port):
        '''
        Constructor
        '''
        self.database = {}
        self._initDatabase()
        self._server_socket = socket.socket()
        self._server_socket.bind((socket.gethostname(), port))
        self._client_socket = None
        self._client_address = None
        
    def _initDatabase(self):
        file = open("data.txt", 'r')
        for line in file:
            line = line.translate(None, '\n')
            data = line.split('|', 3)
            self.database[data[0]] = (data[1], data[2], data[3])
        print "Database read from file"
        print self.database
        
    def run(self):
        self._server_socket.listen(0)
        print "Server is now running"
        while True:
            self._acceptConnection()
        
    def _acceptConnection(self):
        self._client_socket, self._client_address = self._server_socket.accept()
        print "Accepted connection from client", self._client_socket
        self.sendMessage("Connection accepted at server" + str(self._server_socket))
        
    def sendMessage(self, message):
        self._client_socket.send(message)
   
if  __name__ =='__main__':
    server = Server(9999)
    server.run()