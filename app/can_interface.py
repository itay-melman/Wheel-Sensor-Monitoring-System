# can_interface.py
import can

sensor data = {}

class CANInterface(threading.Thread):
    def __init__(self, channel='can0', bustype='socketcan'):
        self.bus = can.interface.Bus(channel=channel, bustype=bustype)

    def send_message(self, arbitration_id, data, extended_id=False):
        message = can.Message(arbitration_id=arbitration_id, data=data, extended_id=extended_id)
        self.bus.send(message)

    def run(self):
        while True:
            message = self.bus.recv()
            if message.arbitration_id == 0x123:
                data = message.data
                sensor_data[data[0]] = data[1]
            
        