#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import sys
import json
import socket

# print results
def print_results():
    print ("\n" + jsoun1_json_variable['name'])
    print(jsoun1_json_variable['weather'][0]["main"])
    temperature_in_city = str(jsoun1_json_variable['main']["temp"])
    temperature_in_city = temperature_in_city[:4]
    print("temp:" + temperature_in_city + "°C")
    humidity_in_city = str(jsoun1_json_variable['main']['humidity'])
    print("humidity:" + humidity_in_city + "%")
    press_in_hPa = str(jsoun1_json_variable['main']['pressure'])
    print("preassure:" + press_in_hPa + " hPa")
    speed_of_wind = str(jsoun1_json_variable['wind']['speed'] * 3.6)
    speed_of_wind = speed_of_wind[:4]
    print("wind-speed: " + speed_of_wind + "km/h")
    try:
        degre_of_wind = jsoun1_json_variable['wind']['deg']
        degre_of_wind = str(degre_of_wind)
        print("wind-deg: " + degre_of_wind)
    except:
        print("wind-deg: -")


#  api server and port
host_api_server_weather_map = "api.openweathermap.org"
port_http = 80

# make socket
oza_super_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  GET request
message_to_api = "GET /data/2.5/weather?q=" + str(sys.argv[2]) + "&APPID=" + str(sys.argv[1]) \
                 + "&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
# connect to api
oza_super_socket.connect((host_api_server_weather_map, port_http))

oza_super_socket.sendto(message_to_api.encode(), (host_api_server_weather_map, port_http))
recived_data = oza_super_socket.recv(156489)

# decode response
decoded_data = recived_data.decode()
decoded_data = decoded_data.split(r'\n')[0]
decoded_data = decoded_data.split('\n')[11]

# ️ put into json
jsoun1_json_variable = json.loads(decoded_data)
if jsoun1_json_variable["cod"] != 200:
    print ("error " + str(jsoun1_json_variable["cod"]) + "\n" + str(jsoun1_json_variable['message']))
    exit()

print_results()

oza_super_socket.close()
