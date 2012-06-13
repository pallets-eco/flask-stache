.. Flask-Stache documentation master file, created by
   sphinx-quickstart on Mon Mar 12 15:35:21 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-Stache
============

.. module:: flask_stache

Flask-Stache lets you use Mustache templates with a Flask application.


Contents
========
* :ref:`installation`
* :ref:`getting-started`
* :ref:`api`
* :doc:`Changelog </changelog>`


.. _installation:

Installation
============

    $ pip install flask-stache


.. _getting-started:

Getting Started
===============

There are two methods of rendering templates when using Flask-Stache: The 
`render_view` and `render_template` methods. They are used like so::

    from flask import Flask
    from flask_stache import render_view, render_template

    class Home(object):
        def msg(self):
            return "Home"

    app = Flask(__name__)
    app.debug = True

    @app.route('/')
    def home():
        return render_view(Home())

    @app.route('/about')
    def about():
        return render_template('about/index', { "msg": "About"})

Notice the view object named `Home` used with `render_view`. The template for 
this view should be a file named `home.mustache` and located at the root of the 
application's template folder::

    <app_root>/templates/home.mustache

Now notice the use of `render_template` in the about view. This should look 
familiar to Flask's `render_template` method. Simply pass the name of the 
template and the template context to this method. The template for the `about` 
viewshould be a file named `index.mustache` and located in a subfolder of the
application's template folder named `about`::

    <app_root>/templates/about/index.mustache

The main difference here is that file extensions are not necessary.


.. _api:

API
===

.. autofunction:: flask_stache.render_view
    
.. autofunction:: flask_stache.render_template


Changelog
=========
.. toctree::
   :maxdepth: 2

   changelog