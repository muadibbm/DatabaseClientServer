'''
Created on 2014-07-09

@author: Mehrdad Dehdashti
'''

import socket
import sys

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
        
    def _getInput(self, promotMessage):
        while True:
            value = raw_input(promotMessage + ': ')
            if(promotMessage == 'Enter Name' and value.translate(None, ' ') == ''):
                print 'Name cannot be empty'
            else:
                break
        return value
        
    def run(self):
        print self._client_socket.recv(1024)
        while True:
            print ("\nPython DB Menu\n" + 
                   "1. Find customer\n" +
                   "2. Add customer\n"+
                   "3. Delete customer\n"+
                   "4. Update customer age\n"+
                   "5. Update customer address\n"+
                   "6. Update customer phone\n"+
                   "7. Print report\n"+
                   "8. Exit\n")
            client_input = raw_input('Select: ')
            if(client_input == '1'):
                self._client_socket.send('1#' + self._getInput('Enter Name'))
                print self._client_socket.recv(1024)
            elif(client_input == '2'):
                self._client_socket.send('2#' + self._getInput('Enter Name') + '#' +
                                         self._getInput('Enter Age') + '#' +  
                                         self._getInput('Enter Address') + '#' + 
                                         self._getInput('Enter Phone'))
                print self._client_socket.recv(1024)
            elif(client_input == '3'):
                self._client_socket.send('3#' + self._getInput('Enter Name'))
                print self._client_socket.recv(1024)
            elif(client_input == '4'):
                self._client_socket.send('4#' + self._getInput('Enter Name') + '#' +
                                         self._getInput('Enter Age'))
                print self._client_socket.recv(1024)
            elif(client_input == '5'):
                self._client_socket.send('5#' + self._getInput('Enter Name') + '#' +
                                         self._getInput('Enter Address'))
                print self._client_socket.recv(1024)
            elif(client_input == '6'):
                self._client_socket.send('6#' + self._getInput('Enter Name') + '#' +
                                         self._getInput('Enter Phone'))
                print self._client_socket.recv(1024)
            elif(client_input == '7'):
                pass
            elif(client_input == '8'):
                self._client_socket.send('8#')
                self._client_socket.close()
                print "Application terminated - Goodbye!"
                sys.exit()
            else:
                print "Invalid input"
        
if  __name__ =='__main__':
    client = Client(9999)
    client.run()