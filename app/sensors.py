# sensors.py
import can
import threading
import time

sensor_data = {"front_left": {"id": 1, "pressure": 0},
               "front_right": {"id": 2, "pressure": 0},
               "rear_left": {"id": 3, "pressure": 0},
               "rear_right": {"id": 4, "pressure": 0}}
sensor_data_lock = threading.Lock()

class SensorSimulator(threading.Thread):
    def __init__(self, wheel_position, simulation_file_path, simulation_interval, id):
        super(SensorSimulator, self).__init__()
        self.wheel_position = wheel_position
        self.simulation_file_path = simulation_file_path
        self.simulation_interval = simulation_interval
        self.id = id
        self.bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

    def run(self):
        while True:
            with open(self.simulation_file_path, "r") as file:
                pressure_value = int(file.readline().strip())
                file.seek(0)

            with sensor_data_lock:
                sensor_data[self.wheel_position] = {"id": self.id, "pressure": pressure_value}

            message = can.Message(arbitration_id=0x123, data=[self.id, pressure_value, 0, 0, 0], extended_id=False)
            self.bus.send(message)

            time.sleep(self.simulation_interval)
