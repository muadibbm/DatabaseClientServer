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
        for line in open("data.txt", 'r'):
            line = line.translate(None, '\n')
            data = line.split('|', 3)
            if(data[0].translate(None, ' ') != ''): # Skipping the record if the name does not exist
                self.database[data[0]] = (data[1].translate(None, ' '), data[2], data[3])
        print "Database read from file"
        print self.database
        
    def run(self):
        self._server_socket.listen(1)
        print "Server is now running"
        if(self._acceptConnection()):
            while True:
                client_request = self._client_socket.recv(1024)
                if(client_request[0] == '1'):
                    if(self.database.has_key(client_request[1:])):
                        self._sendMessage(client_request[1:] + ":" + str(self.database[client_request[1:]]))
                    else:
                        self._sendMessage("Customer not found")
                    
    def _acceptConnection(self):
        self._client_socket, self._client_address = self._server_socket.accept()
        print "Accepted connection from client", self._client_socket
        self._sendMessage("Connection accepted at server" + str(self._server_socket))
        return True
        
    def _sendMessage(self, message):
        self._client_socket.send(message)
   
if  __name__ =='__main__':
    server = Server(9999)
    server.run()