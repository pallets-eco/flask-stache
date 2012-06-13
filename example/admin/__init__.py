
from flask import Blueprint

from flask_stache import render_view, render_template


class Admin(object):
    def msg(self):
        return "Admin"


def create_blueprint():
    bp = Blueprint('admin', __name__, template_folder='templates')

    @bp.route('/')
    def admin():
        return render_view(Admin())

    @bp.route('/books')
    def books():
        return render_template('books/index', {})

    return bp
