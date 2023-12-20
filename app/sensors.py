# sensors.py
import can
import threading
import time

sensor_data = {"front_left": 0, "front_right": 0, "rear_left": 0, "rear_right": 0}
sensor_data_lock = threading.Lock()

class SensorSimulator(threading.Thread):
    def __init__(self, wheel_position, simulation_file_path, simulation_interval):
        super(SensorSimulator, self).__init__()
        self.wheel_position = wheel_position
        self.simulation_file_path = simulation_file_path
        self.simulation_interval = simulation_interval
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan')

    def run(self):
        while True:
            with open(self.simulation_file_path, "r") as file:
                pressure_value = int(file.readline().strip())
                file.seek(0)

            with sensor_data_lock:
                sensor_data[self.wheel_position] = pressure_value

            message = can.Message(arbitration_id=0x123, data=[pressure_value, 0, 0, 0], extended_id=False)
            self.bus.send(message)

            time.sleep(self.simulation_interval)
