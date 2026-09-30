import time
import adafruit_ads7830.ads7830 as ADC
from adafruit_ads7830.analog_in import AnalogIn
import board
import database as db


def main():
    i2c = board.I2C()
    adc = ADC.ADS7830(i2c)

    plant_config = {"plant A": 0, "plant B": 1, "plant C": 2}

    take_reading(adc, i2c, plant_config)
    

def insert_readings(readings, plant_config):
    for i in range(len(readings)):
        name = plant_config[i]
        match name:
            case "plant A":
                with db.engine.connect() as conn:
                    db.reading_insert = db.readings_001.insert().values(date=time.strftime("%Y-%m-%d %H:%M:%S"), moisture_level=readings[i])
                    conn.execute(db.reading_insert)
                    conn.commit()
            case "plant B":
                with db.engine.connect() as conn:
                    db.reading_insert = db.readings_002.insert().values(date=time.strftime("%Y-%m-%d %H:%M:%S"), moisture_level=readings[i])
                    conn.execute(db.reading_insert)
                    conn.commit()
            case _:
                print(f"Unknown plant: {name}")

def take_reading(adc, i2c, plant_config):
    try:
        while True:
            readings = []
            for item in plant_config.values():
                readings.append(AnalogIn(adc, item).value)
            print(f"Plant A: {readings[0]}, Plant B: {readings[1]}, Plant C: {readings[2]}")
            insert_readings(readings, list(plant_config.keys()))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

        
if __name__ == "__main__":
    main()