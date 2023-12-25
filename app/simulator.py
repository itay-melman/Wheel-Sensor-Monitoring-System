# simulator.py
import threading
import time
from sensors import SensorSimulator

def start_sensors():
    simulation_file_path = "sensor_data.txt"
    simulation_interval = 30

    sensors = [
        SensorSimulator("front_left", simulation_file_path, simulation_interval, 1),
        SensorSimulator("front_right", simulation_file_path, simulation_interval, 2),
        SensorSimulator("rear_left", simulation_file_path, simulation_interval, 3),
        SensorSimulator("rear_right", simulation_file_path, simulation_interval, 4),
    ]

    for sensor in sensors:
        sensor.start()

    return sensors

def process_sensor_data(sensor_data):
    print("Received Sensor Data:")
    for wheel, (sensor_id, pressure) in sensor_data.items():
        print(f"{wheel} (ID: {sensor_id}): {pressure}")

def main():
    sensors = start_sensors()
    
    while True:
        with sensors[0].sensor_data_lock:
            # Access the shared sensor_data dictionary
            current_sensor_data = {wheel: (sensor.id, sensor.pressure) for wheel, sensor in sensors[0].sensor_data.items()}

        # Process the received sensor data
        process_sensor_data(current_sensor_data)

        time.sleep(1)

if __name__ == '__main__':
    main()
