from flask import Blueprint, render_template

profiles = Blueprint('other', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/static')


@other.route('/', methods=['GET'])
def index():
    profiles = Profile.query.all()

    return render_template('other/index.html', profiles=profiles)
