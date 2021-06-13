from flask import render_template, request, redirect, Blueprint
from models.request import Request
import repositories.request_repository as request_repository

requests_blueprint = Blueprint("requests", __name__)

@requests_blueprint.route("/requests")
def requests():
    requests = request_repository.select_all()
    print("")
    print(requests[0].song.__dict__)
    print("")
    return render_template("index.html", requests=requests )