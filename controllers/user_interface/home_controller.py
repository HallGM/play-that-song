from flask import render_template, request, redirect, Blueprint
from models.request import Request
import repositories.request_repository as request_repository

ui_home_blueprint = Blueprint("ui_home", __name__)

@ui_home_blueprint.route('/user-interface/<id>')
def ui_home(id):
    return render_template('/user_interface/index.html', id=id, back_button=None)