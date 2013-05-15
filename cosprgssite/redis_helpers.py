__author__ = "Jeremy Nelson"
import datetime
import json
import os
import redis

QUAKER_REDIS = redis.StrictRedis(port=6391)

def load_friend_json(json_filepath,
                     quaker_redis=QUAKER_REDIS):
    friend_file = open(json_filepath, 'rb')
    try:
        friend = json.load(friend_file)
        friend_file.close()
    except ValueError, e:
        friend_file.close()
        print("Cannot load {0} into valid JSON".format(friend_file))
        print("ERROR {0}".format(e))
        return None
    url, friend_key = os.path.split(friend.get('@id'))
    quaker_redis.hset('{0}:prov:Generation'.format(friend_key),
                      'prov:atTime',
                      datetime.datetime.utcnow().isoformat())
    quaker_redis.hset('{0}:prov:Generation'.format(friend_key),
                      'prov:wasGeneratedBy',
                      'http://coloradospringsquakers.org')
    worksAt = friend.pop('worksAt')
    context = friend.pop('@context')
    if friend.has_key('PostalAddress'):
        postal_address = friend.pop('PostalAddress')
        addr_redis_key = 'PostalAddress:{0}'.format(quaker_redis.incr('global PostalAddress'))
        quaker_redis.hset(friend_key,
                          'PostalAddress',
                          addr_redis_key)
        for addr_key, addr_value in postal_address.iteritems():
            quaker_redis.hset(addr_redis_key, addr_key, addr_value)
        quaker_redis.sadd('{0}:occupants'.format(addr_redis_key), friend_key)
    if friend.has_key('parent'):
        parent = friend.pop('parent')
        if type(parent) == list:
            for row in parent:
                stuff, parent_key = os.path.split(row.get('@id'))
                quaker_redis.sadd('{0}:parent'.format(friend_key), parent_key)
    if friend.has_key('sibling'):
        sibling = friend.pop('sibling')
        if type(sibling) == list:
            for row in sibling:
                stuff, sib_key = os.path.split(row.get('@id'))
                quaker_redis.sadd('{0}:sibling'.format(friend_key), sib_key)
        elif type(sibling) == dict:
            print(sibling, type(sibling))
            ## stuff, sib_key = os.path.split(sibling.get('@id'))
            
            ##quaker_redis.hset(friend_key, 'sibling', sib_key)
    if friend.has_key('csq:category'):
        csq_category = friend.pop('csq:category')
        if not quaker_redis.hexists('csq:categories', csq_category.get('csq:code')):
            quaker_redis.hset('csq:categories', csq_category.get('csq:code'),
                              csq_category.get('csq:label'))
        quaker_redis.hset(friend_key, 'csq:category', csq_category.get('csq:code'))
    if friend.has_key('spouse'):
        spouse = friend.pop('spouse')
        stuff, spouse_key = friend.pop('spouse')
        quaker_redis.hset(friend_key, 'spouse', spouse_key)
    for rest_key, rest_value in friend.iteritems():
        if rest_key.startswith('csq:office'):
            pass
        else:
            quaker_redis.hset(friend_key, rest_key, rest_value)
