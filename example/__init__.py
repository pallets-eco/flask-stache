from flask import Flask

from flask_stache import render_view, render_template

from example.admin import create_blueprint


class Home(object):
    def msg(self):
        return "Home"

    def msg2(self):
        return "Partial Content"


class About(object):
    def msg(self):
        return "About"


def create_app():
    app = Flask(__name__)
    app.debug = True

    @app.route('/')
    def home():
        return render_view(Home())

    @app.route('/about')
    def about():
        return render_view(About())

    @app.route('/custom')
    def custom():
        return render_template('custom', {"msg": "Custom"})

    @app.route('/stuff')
    def stuff():
        return render_template('stuff/index', {})

    app.register_blueprint(create_blueprint(), url_prefix='/admin')

    return app
