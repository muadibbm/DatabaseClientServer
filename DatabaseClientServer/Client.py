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
                name = raw_input('Enter Name: ')
                self._client_socket.send("1" + name)
                print self._client_socket.recv(1024)
            elif(client_input == '2'):
                pass
            elif(client_input == '3'):
                pass
            elif(client_input == '4'):
                pass
            elif(client_input == '5'):
                pass
            elif(client_input == '6'):
                pass
            elif(client_input == '7'):
                pass
            elif(client_input == '8'):
                self._client_socket.close()
                print "Application terminated"
                sys.exit()
            else:
                print "Invalid input"
        
if  __name__ =='__main__':
    client = Client(9999)
    client.run()