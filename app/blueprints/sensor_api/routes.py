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


@sensors.route('/post_sensor', methods=['POST'])
def post_sensor():
    data = request.form
    sensor = Sensor(name=data['name'], desc=data['desc'], state=0)

    db.session.add(sensor)
    db.session.commit()

    return jsonify('{"message": "Success"}')


@sensors.route('/update_state/<int:sid>/<int:state>', methods=['PUT'])
def update_state(sid, state):
    sensor = db.get_or_404(Sensor, sid)
    if state == 1 or state == 0:
        sensor.state = state
    else:
        return jsonify('{"message": "Error"}')

    db.session.commit()

    return jsonify('{"message": "Success"}')
