import time
import Adafruit_ADS1x15

def main():
    adc = Adafruit_ADS1x15.ADS1115()

    gain = 1

    try:
        while True:
            readings = read_moisture([0, 1, 2])
            print(f"Plant A: {readings[0]}, Plant B: {readings[1]}, Plant C: {readings[2]}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

def read_moisture(pinList):
    adc = Adafruit_ADS1x15.ADS1115()
    gain = 1
    readings = []
    for item in pinList:
        readings.append(adc.read(item, gain=gain))
    return readings


if __name__ == "__main__":
    main()