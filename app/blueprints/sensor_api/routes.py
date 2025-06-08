from flask import Blueprint, render_template, request, jsonify

from app.app import db
from app.blueprints.sensor_api.models import Sensor

sensors = Blueprint('sensors', __name__, template_folder='templates',
                    static_folder='static', static_url_path='/static')


@sensors.route('/', methods=['GET'])
def index():
    sensors = Sensor.query.all()

    return render_template('sensor_api/index.html', sensors=sensors)


@sensors.route('/register', methods=['GET'])
def register():
    return render_template('sensor_api/register.html')


@sensors.route('/update/<int:sid>', methods=['GET'])
def update(sid):
    sensor = Sensor.query.filter(Sensor.sid == sid).first()

    return render_template('sensor_api/update.html', sensor=sensor)


@sensors.route('/get-all', methods=['GET'])
def get_all_sensors():
    sensors = Sensor.query.all()
    sensors_dict = []

    for s in sensors:
        sensors_dict.append(s.serialize)

    return jsonify(sensors_dict)


@sensors.route('/get-sensor/<int:pid>', methods=['GET'])
def get_sensor(pid):
    sensor = db.session.get(Sensor, pid)

    if sensor is None:
        return render_template('404.html'), 404

    return jsonify(sensor.serialize)


@sensors.route('/post-sensor', methods=['POST'])
def post_sensor():
    data = request.get_json()
    sensor = Sensor(name=data['name'], desc=data['desc'], state=0)

    db.session.add(sensor)
    db.session.commit()

    return jsonify('{"message": "Success"}')


@sensors.route('/update-sensor', methods=['PUT'])
def update_sensor():
    data = request.get_json()
    sensor = Sensor.query.filter(Sensor.sid == data['id']).first()

    sensor.update_info(data)
    db.session.commit()

    return jsonify('{"message": "Success"}')


@sensors.route('/update-state/<int:sid>/<int:state>', methods=['PUT', 'GET'])
def update_state(sid, state):
    sensor = db.get_or_404(Sensor, sid)
    if state == 1 or state == 0:
        sensor.state = state
    else:
        return jsonify({"message": "Error"})

    db.session.commit()

    return jsonify({"message": "Success"})


@sensors.route('/delete-sensor/<sid>', methods=['DELETE'])
def delete_sensor(sid):
    sensor = db.session.get(Sensor, sid)

    db.session.delete(sensor)
    db.session.commit()

    return jsonify({"message": "Success"})
