'''
Created on 2014-07-09

@author: Mehrdad Dehdashti
'''

import socket

class Client(object):
    '''
    Client Class
    '''


    def __init__(self, port):
        '''
        Constructor
        '''
        self._client_socket = socket.socket()
        self._client_socket.connect((socket.gethostname(), port))
        
    def run(self):
        print self._client_socket.recv(1024)
        
if  __name__ =='__main__':
    client = Client(9999)
    client.run()