# -*-: coding: utf-8 -*-

import sys


def hello(name):
  print u'Going to say hello to %(name)s' % { "name": name}
  return name

def tell_year():
  return 2016
