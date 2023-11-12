# Importing the flask module
from flask import Flask
from board import I2C
import Adafruit_DHT as DHT
import adafruit_bh1750 as BH1750

# Create a flask object named app
app = Flask(__name__)

DHT11_pin = 23
i2c = I2C()
sensor = BH1750.BH1750(i2c)


# Once you enter the IP address of Raspberry Pi in the browser, below code will run.
@app.route("/")
def main():
    humi, temp = DHT.read_retry(DHT.DHT11, DHT11_pin)
    lux = sensor.lux
    humi = '{0:0.1f}'.format(humi)
    temp = '{0:0.1f}'.format(temp)
    lux = '{0:0.1f}'.format(lux)
    return f"""{"temperature": "{temp}", "humidity": "{humi}", "lux": "{lux}"}"""


# if code is run from terminal
if __name__ == "__main__":
    # Server will listen to port 80 and will report any errors.
    app.run(host='0.0.0.0', port=80, debug=True)
