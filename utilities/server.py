"""
 Server for schema.org editor
"""
__author__ = "Jeremy Nelson"

import os
import redis

from bottle import post, request, route, run, static_file
from bottle import template, view
## from bottle import jinja2_view as view
## from bottle import jinja2_template as template

from schema_forms import SCHEMA_JSON, get_form


UTILITIES_ROOT = os.path.split(os.path.abspath(__file__))[0]
PROJECT_ROOT = os.path.split(UTILITIES_ROOT)[0]
PROJECT_DIR = "cosprgssite"

REDIS_HOST = 'localhost'
REDIS_PORT = 6391
REDIS_DS = redis.StrictRedis(host=REDIS_HOST,
                             port=REDIS_PORT)


@route('/assets/<type_of:path>/<filename:path>')
def send_asset(type_of, filename):
    """Static file routing

    Parameters:
    type_of -- Type of static file, usual choices are css, js, or img
    filename -- filename of the static file including extension
    """
    local_path = os.path.join(PROJECT_ROOT,
                              PROJECT_DIR,
                              "assets",
                              type_of,
                              filename)
    utility_path = os.path.join(UTILITIES_ROOT,
                                "assets",
                                type_of,
                                filename)
    if os.path.exists(utility_path):
        return static_file(filename,
                           root=os.path.join(UTILITIES_ROOT,
                                             "assets",
                                             type_of))
    elif os.path.exists(local_path):
        return static_file(filename,
			   root=os.path.join(PROJECT_ROOT,
                                             PROJECT_DIR,
                                             "assets",
                                             type_of))



@post("/crud")
def operations():
    "Routes CRUD operations"
    output = 'Form values:'
    for name, value in request.forms.iteritems():
        output += "{0}={1}<br>".format(name, value)
    return output


@route("/choose")
def choose():
    "Displays Schema.org Entity Form"
    entity_name = request.query.schema_types
    form = get_form(entity_name)
    return template('schema_form',
                    name=entity_name,
                    form=form())



@route("/")
def index():
    "Default view for editor"
    return template('index',
                    schema_types=sorted(SCHEMA_JSON['types'].keys()))

run(host='0.0.0.0', port=9042, reloader=True)
