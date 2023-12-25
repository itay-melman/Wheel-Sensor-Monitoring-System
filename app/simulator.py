# simulator.py
import time

def start_sensors():
    from sensors import SensorSimulator

    simulation_file_path = "sensor_data.txt"
    simulation_interval = 30

    sensors = [
        SensorSimulator("front_left", simulation_file_path, simulation_interval),
        SensorSimulator("front_right", simulation_file_path, simulation_interval),
        SensorSimulator("rear_left", simulation_file_path, simulation_interval),
        SensorSimulator("rear_right", simulation_file_path, simulation_interval),
    ]

    for sensor in sensors:
        sensor.start()

    return sensors

def main():
    sensors = start_sensors()
    while True:
        #main logic goes here
        time.sleep(1)

if __name__ == '__main__':
    main()
