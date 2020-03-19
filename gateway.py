import serial
import datetime
import requests


ser = serial.Serial('/dev/ttyACM0', 9600, timeoout=10)
data = {}


is_first = True


while True:
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
    lux = ser.readline().decode('utf-8')
    data['time'] = now
    data['lux'] = lux

    if is_Frist:
        is_first = False
    else:
        print(data)
        response = requests.post('http://160.16.210.86:16074/lux', data=data)
        print(response)


ser.close()
