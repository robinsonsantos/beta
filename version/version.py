# -*- coding: utf-8 -*-

PROTO = '2'
MAJOR = '1'
MINOR = '7'

def major_minor():
    return '%s.%s' % (MAJOR, MINOR)

def full():
    return '%s-%s.%s' % (PROTO, MAJOR, MINOR)

def compat(client, server):
    return bool(client == server)
