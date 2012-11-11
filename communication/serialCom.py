'''
Created on Nov 7, 2012

@author: Ted Carancho
'''
import serial
import time

class AQSerial(object):
    '''
    This handles all serial communication
    '''
    
    def __init__(self):
        self.comm = None
        self.availablePorts = None

    def connect(self, port, baud):
        self.comm = serial.Serial(port, baud, timeout=1) 
        
    def disconnect(self):
        self.comm.close()
        
    def write(self, data):
        self.comm.write(bytes(data.encode('utf-8')))
        
    def read(self):
        response = self.comm.readline().decode('utf-8')
        return response.rstrip('\r\n')
    
    def dataAvailable(self):
        return self.comm.inWaiting()
        
    def detectPorts(self):
        # scan for available ports. return a list of tuples (num, name)
        for i in range(256):
            try:
                s = serial.Serial(i)
                self.availablePorts.append((i, s.portstr))
                s.close()
            except serial.SerialException:
                pass
        return self.availablePorts
