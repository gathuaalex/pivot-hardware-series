import network
import esp32
import utime

import gc
gc.collect()

from microdot_asgi import Microdot,Response
from html import main_page

ssid = 'CISCO ACADEMY'
password = 'netcad2016'

station = network.WLAN(network.STA_IF)
station.active(True)

while station.isconnected() == False:
    try:
        station.connect(ssid, password)
    except  OSError:
        pass
    utime.sleep(2)

print('Connection successful')
print(station.ifconfig())

Response.default_content_type = 'text/html'
app = Microdot()

@app.route('/')
def index(request):
    return main_page

@app.route('/temperature')
def temperature(request):
    b_temp=esp32.raw_temperature()
    measured_temp = (b_temp - 32) / 1.8
    return str(round(measured_temp,2))
@app.route('/humidity')
def humidity(request):
    return '45.2'


app.run(host='',port=80, debug=True)