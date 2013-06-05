__author__ = "Jeremy Nelson"

import datetime
import json
import os
import urllib2
import wtforms

from bottle import request, route, run, static_file
from bottle import jinja2_view as view
from bottle import jinja2_template as template

PROJECT_ROOT = os.path.split(os.path.abspath(__file__))[0]

SCHEMA_RDFS_URL = 'http://schema.rdfs.org/all.json'
SCHEMA_JSON = json.load(urllib2.urlopen(SCHEMA_RDFS_URL))

SCHEMA_DATATYPE_MAP = {u'Boolean': wtforms.BooleanField,
                       u'DataType': wtforms.TextField,
                       u'Date': wtforms.DateField,
                       u'DateTime': wtforms.DateTimeField,
                       u'Float': wtforms.FloatField,
                       u'Integer': wtforms.IntegerField,
                       u'Number': wtforms.DecimalField,
                       u'Text': wtforms.TextField,
                       u'Time': wtforms.TextField,
                       u'URL': wtforms.TextField}

@route('/assets/<type_of:path>/<filename:path>')
def send_asset(type_of,filename):
    local_path = os.path.join(PROJECT_ROOT,
                              "assets",
                              type_of,
                              filename)
    if os.path.exists(local_path):
        return static_file(filename,
			   root=os.path.join(PROJECT_ROOT,
                                             "assets",
                                             type_of))


@route("/choose")
def choose():
    entity_name = request.query.schema_types
    if SCHEMA_JSON['types'].has_key(entity_name) is False:
        raise ValueError("{0} not a schema.org type.".format(entity_name))
    fields = {}
    properties = SCHEMA_JSON['types'][entity_name].get('properties')
    properties.extend(
        SCHEMA_JSON['types'][entity_name].get('specific_properties'))
    for name in sorted(properties):
        property_types = SCHEMA_JSON['properties'][name].get('ranges')
        print('{0} {1} Types: {2}'.format(entity_name,
                               name,
                               ' '.join(property_types)))
        if not SCHEMA_DATATYPE_MAP.has_key(property_types[0]):
            field_class = wtforms.TextField 
        fields[name.lower()] = type(SCHEMA_DATATYPE_MAP[property_types[0]],
                                    (name,))
    form = type("{0}Form".format(entity_name),
                (Form,),
                fields)
    return template('schema_form',
                    form=form())

@route("/")
def index():
    return template('index',
                    schema_types=sorted(SCHEMA_JSON['types'].keys()))

run(host='0.0.0.0', port=9042)
