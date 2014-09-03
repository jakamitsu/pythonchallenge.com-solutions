#!/usr/bin/env python3
"""
This script solves all challenges from www.pythonchallenge.com
Created by Pawel Chiberski
"""
import os, sys

# Decorator for challenges functions
challenges = {}
def challenge(n):
  def decorator(f):
    def wrapper(*args, **kwargs):
      print('')
      print('######################')
      print('# Begin challenge %s #' % format(n, '02d'))
      print('######################')
      f(*args, **kwargs)
    challenges[n] = wrapper
    return wrapper
  return decorator

# Challenges code will go here
@challenge(0)
def Challenge0():
  startAddr = 'http://www.pythonchallenge.com/pc/def/0.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  inputData = 2 ** 38
  
  resultAddr += '%d.html' % inputData
  print(resultAddr)

@challenge(1)
def Challenge1():
  from urllib.parse import urlparse
  startAddr = 'http://www.pythonchallenge.com/pc/def/map.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  inputData = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq \
  ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm \
  jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
  
  inTab = 'abcdefghijklmnopqrstuvwxyz'
  outTab ='cdefghijklmnopqrstuvwxyzab'
  tranTab = str.maketrans(inTab, outTab)
  
  outputData = inputData.translate(tranTab)
  
  cUrl = urlparse(startAddr)
  rUrl = cUrl.path.split('/')[-1].split('.')[0].translate(tranTab)

  resultAddr += rUrl + '.html'
  print(resultAddr)

if __name__ == '__main__':
  to_run = sorted(challenges.keys())
  if len(sys.argv) > 1:
    try:
      n = int(sys.argv[1])
    except ValueError:
      print('Usage: %s [n] (where n is an integer)' % sys.argv[0])
      sys.exit(1)
    if not n in challenges:
      print('No such challenge: %d' %n)
      sys.exit(1)
    to_run = [n]
  for n in to_run:
    challenges[n]()
