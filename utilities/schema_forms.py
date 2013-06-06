"""
 wtforms-based Schema.org Forms
"""
__author__ = "Jeremy Nelson"

import json
import re
import wtforms
import urllib2

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

        
def convert(name):
    """Helper function converts a name in CamelCase to camel_case format

    >> convert('accessPoint')
    >> 'access_point'
    >> convert('ColoradoSprings')
    >> 'colorado_springs'
    Parameters:
    name -- CamelCase name
    """
    temp_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', temp_str).lower()


def get_form(entity_name):
    """
    Function returns a WTForm derived form based on a schema.org entity name

    >> form = get_form('Person')
    
    Parameters:
    entity_name -- Name of entity
    """
    if SCHEMA_JSON['types'].has_key(entity_name) is False:
        raise ValueError("{0} not a schema.org type.".format(entity_name))
    properties = SCHEMA_JSON['types'][entity_name].get('properties')
    properties.extend(
        SCHEMA_JSON['types'][entity_name].get('specific_properties'))
    form_listing = {}
    for name in sorted(properties):
        fields = {}
        property_types = SCHEMA_JSON['properties'][name].get('ranges')
        #print "{0} {1} {2}".format(entity_name, name, ','.join(property_types))
        for row in property_types:
            if SCHEMA_JSON['types'].has_key(row):
                json_info = SCHEMA_JSON['types'].get(row)
                choices = [(None, row)]
                subtypes = json_info.get('subtypes')
                if len(subtypes) > 0:
                    for row in subtypes:
                        choices.append((row, row))
                fields[convert(row)] = wtforms.SelectField(choices=choices)
            elif SCHEMA_DATATYPE_MAP.has_key(row):
                fields[convert(row)] = SCHEMA_DATATYPE_MAP[property_types[0]]()
            else:
                fields[convert(row)] = wtforms.TextField()
                
             
        property_form = type("{0}{1}Form".format(entity_name, name),
                             (wtforms.Form,),
                             fields)
        form_listing[convert(name)] = wtforms.FormField(property_form)
        
    return type("{0}Form".format(entity_name),
                (wtforms.Form,),
                form_listing)        
        
    
