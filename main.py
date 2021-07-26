# Short program with an example on how to create the sensor class and read a value from it. This folder contains the
# some of the most common libraries (numpy and matplotlib) for further data visualization and analysis

from DSCUSBSensor import Sensor

if __name__ == '__main__':

    sensor = Sensor(4#COMPort) #Create the connection with the sensor and open the port

    value = sensor.readvalue() #Read a value in the sensor

    sensor.close() #Close the port and end the connection with the sensor
