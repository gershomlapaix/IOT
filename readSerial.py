#!/usr/bin/env python3
import serial
import requests

url = 'http://insecure.benax.rw/iot/'

ser = serial.Serial(
    port='/dev/ttyUSB0',  # plz change this according to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.flush()
if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f = open("data.txt", "a")
            requestData = {
                'device': 'Gershom-Moss-Egide-Group',
                'distance': line
            }
            response = requests.post(url, data=requestData)
            f.write(line)
            f.write("\n")
            f.close()
            print(line)
