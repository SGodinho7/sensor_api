from flask import Blueprint, render_template

sensors = Blueprint('sensors', __name__, template_folder='templates',
                    static_folder='static', static_url_path='/static')


@sensors.route('/', methods=['GET'])
def index():
    return render_template('sensor_api/index.html')
