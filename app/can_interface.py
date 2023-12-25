#can_interface.py
import can
import threading

class WheelPositionEnum:
    FRONT_LEFT = 1
    FRONT_RIGHT = 2
    REAR_LEFT = 3
    REAR_RIGHT = 4

# Dictionary to map sensor IDs to wheel positions
SENSOR_ID_TO_WHEEL_POSITION = {
    WheelPositionEnum.FRONT_LEFT: "front_left",
    WheelPositionEnum.FRONT_RIGHT: "front_right",
    WheelPositionEnum.REAR_LEFT: "rear_left",
    WheelPositionEnum.REAR_RIGHT: "rear_right",
}

sensor_data = {}

class CANInterface(threading.Thread):
    def __init__(self, channel='can0', bustype='socketcan'):
        self.bus = can.interface.Bus(channel=channel, bustype=bustype)

    def send_message(self, arbitration_id, data, extended_id=False):
        message = can.Message(arbitration_id=arbitration_id, data=data, extended_id=extended_id)
        self.bus.send(message)

    def get_wheel_position_from_id(self, sensor_id):
        return SENSOR_ID_TO_WHEEL_POSITION.get(sensor_id)

    def run(self):
        while True:
            message = self.bus.recv()
            if message.arbitration_id == 0x123:
                sensor_id, pressure_value = message.data[0], message.data[1]
                wheel_position = self.get_wheel_position_from_id(sensor_id)

                with sensor_data_lock:
                    sensor_data[wheel_position] = pressure_value
