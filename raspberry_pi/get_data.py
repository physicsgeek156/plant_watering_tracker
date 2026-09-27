import time
import adafruit_ads7830.ads7830 as ADC
from adafruit_ads7830.analog_in import AnalogIn
import board

from database import plants

def main():
    try:
        while True:
            readings = read_moisture([0, 1, 2])
            print(f"Plant A: {readings[0]}, Plant B: {readings[1]}, Plant C: {readings[2]}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

def read_moisture(pinList):
    i2c = board.I2C()
    adc = ADC.ADS7830(i2c)
    readings = []
    for item in pinList:
        readings.append(AnalogIn(adc, item).value)
    return readings


if __name__ == "__main__":
    main()