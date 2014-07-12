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
        self._database = {}
        self._init_database()
        self._server_socket = socket.socket()
        self._server_socket.bind((socket.gethostname(), port))
        self._client_socket = None
        self._client_address = None
        
    def _init_database(self):
        dataFile = open("data.txt", 'r')
        for line in dataFile:
            line = line.translate(None, '\n')
            data = line.split('|', 3)
            if(data[0].translate(None, ' ') != ''): # Skipping the record if the name does not exist
                self._database[data[0]] = (data[1].translate(None, ' '), data[2], data[3])
        dataFile.close()
        print "_database read from file"
        print self._database
        
    def run(self):
        print "Server is now running"
        while True:
            self._server_socket.listen(1)
            if(self._acceptConnection()):
                while True:
                    client_request = self._client_socket.recv(1024)
                    values = client_request.split('#')
                    if(values[0] == '1'):
                        self._findCustomer(values[1])
                    elif(values[0] == '2'):
                        self._addCustomer(values[1], values[2], values[3], values[4])
                    elif(values[0] == '3'):
                        self._deleteCustomer(values[1])
                    elif(values[0] == '4'):
                        self._updateCustomerAge(values[1], values[2])
                    elif(values[0] == '5'):
                        self._updateCustomerAddress(values[1], values[2])
                    elif(values[0] == '6'):
                        self._updateCustomerPhone(values[1], values[2])
                    elif(values[0] == '7'):
                        pass
                    elif(values[0] == '8'):
                        break
                    self._updateDatabase()
                    
    def _acceptConnection(self):
        self._client_socket, self._client_address = self._server_socket.accept()
        print "Accepted connection from client", self._client_socket
        self._sendMessage("Connection accepted at server" + str(self._server_socket))
        return True
        
    def _sendMessage(self, message):
        self._client_socket.send(message)
    
    def _updateDatabase(self):
        dataFile = open("data.txt", 'w')
        for entry in self._database:
            dataFile.write(entry + '|' + self._database[entry][0] + '|' + self._database[entry][1] + '|' + self._database[entry][2] + '\n')
        dataFile.close()
            
    def _findCustomer(self, name):
        if(self._database.has_key(name)):
            self._sendMessage(name + ":" + str(self._database[name]))
        else:
            self._sendMessage("Customer not found")
            
    def _addCustomer(self, name, age, address, phone):
        if(self._database.has_key(name) == False):
            self._database[name] = (age, address, phone)
            self._sendMessage("Customer " + name + " has been added")
        else:
            self._sendMessage("Customer already exists")
    
    def _deleteCustomer(self, name):
        if(self._database.has_key(name)):
            self._database.pop(name)
            self._sendMessage("Customer " + name + " has been deleted")
        else:
            self._sendMessage("Customer does not exist")
    
    def _updateCustomerAge(self, name, age):
        if(self._database.has_key(name)):
            self._database[name] = (age, self._database[name][1], self._database[name][2])
            self._sendMessage("Customer " + name + "'s age has been updated to " + age)
        else:
            self._sendMessage("Customer not found")
    
    def _updateCustomerAddress(self, name, address):
        if(self._database.has_key(name)):
            self._database[name] = (self._database[name][0], address, self._database[name][2])
            self._sendMessage("Customer " + name + "'s address has been updated to " + address)
        else:
            self._sendMessage("Customer not found")
    
    def _updateCustomerPhone(self, name, phone):
        if(self._database.has_key(name)):
            self._database[name] = (self._database[name][0], self._database[name][1], phone)
            self._sendMessage("Customer " + name + "'s phone has been updated to " + phone)
        else:
            self._sendMessage("Customer not found")
    
    def _printReport(self):
        pass
   
if  __name__ =='__main__':
    server = Server(9999)
    server.run()