import requests
import serial
import os

URL = 'https://tinyprints.herokuapp.com/api/'
LOCAL = 'http://127.0.0.1:5000/api/'
API_KEY = os.environ.get('TINYPRINTS_API_PASSWORD') or 'dev'


URL

ser = serial.Serial('/dev/serial0')



def get_winner():
    r = requests.get(f'{URL}lastwinner')
    return r


def close(pw):
    r = requests.post(f'{URL}close', data={'pw': pw})
    return r


r = close(API_KEY)
print(r.raise_for_status())

r = get_winner()
print(r.raise_for_status())


tinyprint = r.json()
print(tinyprint)
# {
#     'created': 'Mon, 18 Jan 2021 00:28:41 GMT',
#     'id': 4,
#     'text': '\n\n _._     _,-\'""`-._\r\n(,-.`._,\'(       |\\`-/|\r\n    `-.-\' \\ )-`( , o o)\r\n          `-    \\`_`"\'-',
#     'title': 'sneaking cat',
#     'votes': 2,
#     'voting_closed_timestamp': 'Tue, 26 Jan 2021 22:20:34 GMT'
# }


ser.write(b'\x1b\x21\x00') # reset
ser.write(tinyprint.get('title').encode())
ser.write('\n'.encode())
ser.write(tinyprint.get('text').encode())
ser.write('\n'.encode())
ser.write('#{}  upvotes: {}\n'.format(tinyprint.get('id'), tinyprint.get('votes')).encode())
ser.write(tinyprint.get('created').encode())
ser.write('\n\n\n'.encode())

