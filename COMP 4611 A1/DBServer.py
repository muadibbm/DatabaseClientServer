'''
Created on 2014-07-08
@author: Mehrdad Dehdashti
'''

import socket

class DBServer(object):
    '''
    The DBServer Class
    '''

    def __init__(self, port):
        '''
        Constructor
        '''
        self._database = {}
        self._client_socket = None
        self._client_address = None
        self._server_socket = socket.socket()
        self._server_socket.bind((socket.gethostname(),port))
        
        self._server_socket.listen(0)
        print "server is running"
        
    def initDatabase(self):
        databaseFile = open('data.txt', 'r')
        for line in databaseFile:
            line = line.translate(None, '\n')
            data = line.split('|', 3)
            self._database[data[0]] = (data[1], data[2], data[3])
        databaseFile.close()
        print 'Database read from file:'
        print self._database
            
        
    def run(self):
        while True:
            self._client_socket, self._client_address =  self._server_socket.accept()
            print "Connection accepted from client", str(self._client_socket)
            self.sendMessage("Connection accepted at server " + str( self._server_socket))
            
    def sendMessage(self, message):
        self._client_socket.send(message)
            
if __name__ == '__main__':
    databaseServer = DBServer(9999) # Create the database server
    databaseServer.initDatabase()
    databaseServer.run()