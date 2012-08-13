"""
Flask-Stache
------------

Simple mustache templating for Flask applications

Links
`````

* `documentation <http://packages.python.org/Flask-Stache/>`_
* `source <https://github.com/mattupstate/flask-stache>`_
* `development version
  <https://github.com/mattupstate/flask-stache/raw/develop#egg=Flask-Stache-dev>`_

"""

from setuptools import setup

setup(
    name='Flask-Stache',
    version='0.1.1',
    url='https://github.com/mattupstate/flask-stache',
    license='MIT',
    author='Matthew Wright',
    author_email='matt@nobien.net',
    description='Simple mustache templating for Flask applications',
    long_description=__doc__,
    py_modules=['flask_stache'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pystache'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
