# api.py
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from sensors import sensor_data, sensor_data_lock
from can_interface import CANInterface

can_interface = CANInterface()

class WheelStatus(Resource):
    def get(self):
        with sensor_data_lock:
            return jsonify(sensor_data)

# API endpoint
api.add_resource(WheelStatus, '/wheel-status')

if __name__ == '__main__':
    app.run(debug=True)
