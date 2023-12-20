# can_interface.py
import can

class CANInterface:
    def __init__(self, channel='can0', bustype='socketcan'):
        self.bus = can.interface.Bus(channel=channel, bustype=bustype)

    def send_message(self, arbitration_id, data, extended_id=False):
        message = can.Message(arbitration_id=arbitration_id, data=data, extended_id=extended_id)
        self.bus.send(message)
