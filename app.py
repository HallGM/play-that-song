from flask import Flask, render_template, redirect

from controllers.song_controller import songs_blueprint
from controllers.user_controller import users_blueprint
from controllers.request_controller import requests_blueprint
from controllers.user_interface.home_controller import ui_home_blueprint


app = Flask(__name__)

app.register_blueprint(songs_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(requests_blueprint)
app.register_blueprint(ui_home_blueprint)

@app.route('/')
def home():
    return redirect('/requests')

if __name__ == '__main__':
    app.run(debug=True)