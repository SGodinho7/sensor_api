from flask import Blueprint, render_template, request, jsonify

sensors = Blueprint('sensors', __name__, template_folder='templates',
                    static_folder='static', static_url_path='/static')


@sensors.route('/', methods=['GET'])
def index():
    return render_template('sensor_api/index.html')


@sensors.route('/register', methods=['GET'])
def register():
    return render_template('sensor_api/register.html')


@sensors.route('/post_sensor', methods=['POST'])
def post_sensor():
    data = request.form

    return jsonify('{"message": "Success"}')
