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

@challenge(2)
def Challenge2():
  from urllib.request import urlopen
  startAddr = 'http://www.pythonchallenge.com/pc/def/ocr.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  
  request = urlopen(startAddr)
  rData = request.read().decode()
  
  tmpMarker = 'find rare characters in the mess below:'
  startIndex = str(rData).find(tmpMarker) + len(tmpMarker)
  
  outputData = ''
  for i in range (startIndex, len(rData)):
    if str(rData[i]).isalpha():
      outputData += str(rData[i])
      
  resultAddr += outputData + '.html'
  print(resultAddr)

@challenge(3)
def Challenge3():
  from urllib.request import urlopen
  startAddr = 'http://www.pythonchallenge.com/pc/def/equality.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  
  request = urlopen(startAddr)
  rData = request.read().decode()
  
  tmpMarker = '<!--'
  startIndex = str(rData).find(tmpMarker) + len(tmpMarker)
  
  outputData = ''
  for i in range(startIndex+4, len(rData)-4):
    if rData[i].islower():
      if not rData[i-4].isupper() and not rData[i+4].isupper():
        if rData[i-3].isupper() and rData[i-2].isupper() and \
        rData[i-1].isupper() and rData[i+1].isupper() and \
        rData[i+2].isupper() and rData[i+3].isupper():
          outputData += rData[i]
  
  resultAddr += outputData + '.html'
  print(resultAddr)

@challenge(4)
def Challenge4():
  from urllib.request import urlopen
  startAddr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  param = '?nothing='
  
  n = '12345'
  
  tmpMarker = 'next nothing is '
  
  while n != 'finish':
    tmpAddr = startAddr + param + n
    tmpRequest = urlopen(tmpAddr)
    tmpData = tmpRequest.read().decode()
    n = ''
    if str(tmpData).find(tmpMarker) > 0:
      sys.stdout.write('.')
      sys.stdout.flush()
      for i in range(str(tmpData).find(tmpMarker) + len(tmpMarker), 
        len(tmpData)):
        if str(tmpData[i]).isdigit():
          n += str(tmpData[i])
    elif str(tmpData).find('Divide by two and keep going.') > 0:
      tmp = tmpAddr.split('=')[1]
      n = str(int(tmp) / 2)
    elif str(tmpData).find('.html') > 0:
      resultAddr += tmpData
      n = 'finish'
    else:
      print('')
      print(tmpAddr)
      print(tmpData)
      n = input('What is the next nothing? (type finish to exit) ')
  
  print('')
  print(resultAddr)
  
@challenge(5)
def Challenge5():
  import pickle
  from urllib.request import urlopen

  startAddr = 'http://www.pythonchallenge.com/pc/def/peak.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  
  request = urlopen(startAddr)
  rData = request.read().decode()

  tmp = '<peakhell src="'
  startMarker = str(rData).find(tmp) + len(tmp)
  
  endMarker = str(rData).find('"/>', startMarker)
  
  file = rData[startMarker:endMarker] 
  
  tmpRequest = urlopen(resultAddr + file)
  tmpData = tmpRequest.read()
  
  inputData = pickle.loads(tmpData)
  
  for row in inputData:
    displ = ''
    for col in row:
      for i in range(col[1]):
        displ += str(col[0])
    print(displ)
    
  resp = input('What word do you see? ')
  
  resultAddr += resp + '.html'
  print(resultAddr)

@challenge(6)
def Challenge6():
  from urllib.request import urlopen
  import zipfile

  startAddr = 'http://www.pythonchallenge.com/pc/def/channel.zip'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  
  request = urlopen(startAddr)
  rData = request.read()
  
  zipFile = open('channel.zip', 'wb')
  zipFile.write(rData)
  zipFile.close()
  
  n = '90052'
  
  archiveFile = zipfile.ZipFile('channel.zip')
  fileName = '%s.txt'
  
  comments = []
  
  tmpMarker = 'Next nothing is '
  
  while n != '':
    comments.append(archiveFile.getinfo(fileName % n).comment.decode())
    tmpData = archiveFile.read(fileName % n).decode()
    n = ''
    for i in range(str(tmpData).find(tmpMarker) + len(tmpMarker), len(tmpData)):
      if str(tmpData[i]).isdigit():
        n += str(tmpData[i])

  print(''.join(comments))
  
  tmp = input('What word do you see? ')
  
  tmpRequest = urlopen(resultAddr + tmp + '.html')
  tmpData = tmpRequest.read().decode()
  
  resultAddr += input('What is the answer? ') + '.html'
  print(resultAddr)
  
@challenge(7)
def Challenge7():
  from urllib.request import urlopen
  from PIL import Image
  import io

  startAddr = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/'
  
  request = urlopen(startAddr)
  rData = request.read()
  
  img = Image.open(io.BytesIO(rData))
  
  msg = ''
  pixels = []
  for x in range(0, img.size[0], 7):
    pixels.append(img.getpixel((x, img.size[1]/2)))
  
  characters = []
  for p in pixels:
    if p[0] == p[1] == p[2]:
      characters.append(chr(p[0]))
  msg = ''.join(characters)
  msg = msg[msg.find('[')+1:-1].split(', ')
  
  page = ''
  for c in msg:
    page += chr(int(c))
  
  resultAddr += page + '.html'
  print(resultAddr)

@challenge(8)
def Challenge8():
  from urllib.request import urlopen
  import bz2
  import binascii

  startAddr = 'http://www.pythonchallenge.com/pc/def/integrity.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/def/good.html'

  request = urlopen(startAddr)
  rData = request.read().decode()

  un_p = "b'" + rData[rData.find("un: '")+5:
    rData.find("'", rData.find("un: '")+6)] + "'"
  pw_p = "b'" + rData[rData.find("pw: '")+5:
    rData.find("'", rData.find("pw: '")+6)] + "'"

  un = bz2.decompress(eval(un_p)).decode()
  pw = bz2.decompress(eval(pw_p)).decode()
  
  print(resultAddr)
  print('Username: ' + un, '\nPassword: ' + pw)
  
@challenge(9)
def Challenge9():
  import urllib.request
  from PIL import Image
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/good.html'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 
  
  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)
  rData = request.read().decode()
  
  first = rData[rData.find('first:')+7:
    rData.find('second:')].replace('\n', '').split(',')
  second = rData[rData.find('second:')+8:
    rData.find('-->', rData.find('second:'))].replace('\n', '').split(',')
  
  third = first + second
  
  img = Image.new('RGB', (640,480))
  
  for c in range(0, len(third), 2):
    x = int(third[c])
    y = int(third[c+1])
    
    img.putpixel((x, y), 255)
  img.save('dots.png')
  
  print('Open dots.png to see the image.')
  resultAddr += 'bull.html'
  print(resultAddr)
  
@challenge(10)
def Challenge():
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 
  a = ['1']
  
  while len(a) < 31:
      prev_item = a[-1]
      char = prev_item[0]
      ch_count = 0
      tmp = []
      for c in prev_item:
        if c == char:
          ch_count += 1
        else:
          tmp.append(str(ch_count) + char)
          char = c
          ch_count = 1
      tmp.append(str(ch_count) + char)
      a.append(''.join(tmp))
  resultAddr += str(len(a[30])) + '.html'
  print(resultAddr)
  
@challenge(11)
def Challenge11():
  import urllib.request
  from PIL import Image
  import io
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 

  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)

  rData = request.read()
  
  img = Image.open(io.BytesIO(rData))
  img.save('cave.jpg')
  newsize = (int(img.size[0]/2), int(img.size[1]/2))
  img_odd = Image.new('RGB', newsize)
  img_even = Image.new('RGB', newsize)
  
  for x in range(0, img.size[0]-2, 2):
    for y in range(0, img.size[1]-2, 2):
      img_even.putpixel((int(x/2), int(y/2)), img.getpixel((x, y)))
      img_odd.putpixel((int(x/2) + 1, int(y/2) + 1), img.getpixel((x+1, y+1)))
  
  img_even.save('even.jpg')
  img_odd.save('odd.jpg')
  
  print('Look at the generated images for a clue.')
  resultAddr += 'evil.html'
  print(resultAddr)

@challenge(12)
def Challenge12():
  import urllib.request
  from PIL import Image
  import io
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 

  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)

  rData = request.read()
  
  f1 = open('img1.jpg', 'wb')
  f2 = open('img2.png', 'wb')
  f3 = open('img3.gif', 'wb')
  f4 = open('img4.png', 'wb')
  f5 = open('img5.jpg', 'wb')
  
  f1.write(rData[0::5])
  f2.write(rData[1::5])
  f3.write(rData[2::5])
  f4.write(rData[3::5])
  f5.write(rData[4::5])
  
  f1.close()
  f2.close()
  f3.close()
  f4.close()
  f5.close()

  print('Look at generated images for a clue')
  resultAddr += 'disproportional.html'
  print(resultAddr)
  
@challenge(13)
def Challenge13():
  import xmlrpc.client
  import urllib.request
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 

  XMLRPCserver = xmlrpc.client.Server(
    'http://www.pythonchallenge.com/pc/phonebook.php'
  )

  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)

  rData = request.read().decode()
  
  evilName = rData.split()[0]
  
  resultAddr += XMLRPCserver.phone(evilName).split('-')[1].lower() + '.html'
  print(resultAddr)

@challenge(14)
def Challenge14():
  import urllib.request
  from PIL import Image
  import io
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/wire.png'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 

  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)

  rData = request.read()
  
  img = Image.open(io.BytesIO(rData))
  resImg = Image.new(img.mode, (100, 100), (0, 0, 0))
  
  pos_x = pos_y = 0
  dir_x = 1
  dir_y = 0
  min_x = min_y = 0
  max_x = max_y = 99
  
  for i in range(10000):
    resImg.putpixel((pos_x, pos_y), img.getpixel((i, 0)))
    if dir_x == 1 and pos_x == max_x:
      dir_x = 0
      dir_y = 1
      min_y += 1
    elif dir_x == -1 and pos_x == min_x:
      dir_x = 0
      dir_y = -1
      max_y -= 1
    elif dir_y == 1 and pos_y == max_y:
      dir_x = -1
      dir_y = 0
      max_x -= 1
    elif dir_y == -1 and pos_y == min_y:
      dir_x = 1
      dir_y = 0
      min_x += 1
    pos_x += dir_x
    pos_y += dir_y
  resImg.save('spiral.png')
  
  print('Look at generated image for a clue.')
  resultAddr += 'uzi.html'
  print(resultAddr)
  
@challenge(15)
def Challenge15():
  import datetime
  
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 
  dates = []
  
  for year in range(1586, 1997, 10):
    d1 = datetime.date(year, 3, 1) - datetime.timedelta(days=1)
    d2 = datetime.date(year, 1, 26)
    
    if d1.day == 29:
      if d2.weekday() == 0:
        dates.append(d2)
  
  print("The date you are looking for is: %s" %
    (dates[-2] + datetime.timedelta(days=1)))
  print("This is the birthday of Mozart")
  resultAddr += 'mozart.html'
  print(resultAddr)

@challenge(16)
def Challenge16():
  import urllib.request
  from PIL import Image
  import io
  
  startAddr = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
  resultAddr = 'http://www.pythonchallenge.com/pc/return/' 

  auth_handler = urllib.request.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='inflate',
                            uri=startAddr,
                            user='huge',
                            passwd='file')
  opener = urllib.request.build_opener(auth_handler)
  urllib.request.install_opener(opener)
  request = urllib.request.urlopen(startAddr)

  rData = request.read()
  
  img = Image.open(io.BytesIO(rData))
  resImg = img
  
  toFind = 195
  
  for row in range(resImg.size[1]):
    rowBoundry = 0, row, resImg.size[0], row + 1
    rowData = resImg.crop(rowBoundry)
    rowString = list(rowData.tostring())
    indx = rowString.index(toFind) + 2
    rowString = rowString[indx:] + rowString[:indx]
    tmp = b''
    for b in rowString:
      tmp += bytes([b])
    rowString = tmp
    rowData.fromstring(rowString)
    resImg.paste(rowData, rowBoundry)

  resImg.save('result.gif')
  print('Look at generated image for a clue.')
  resultAddr += 'romance.html'
  print(resultAddr)
  
@challenge(17)
def Challenge17():
  import urllib.request
  import urllib.parse
  from http import cookiejar
  import bz2
  import xmlrpc.client
  
  startAddr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
  startAddr += '?busynothing='
  
  next_nothing = '12345'
  
  cookie_jar = cookiejar.CookieJar()
  cookie_processor = urllib.request.HTTPCookieProcessor(cookie_jar)
  opener = urllib.request.build_opener(cookie_processor)
  message = ""
  marker = 'and the next busynothing is '
  
  print('Decrypting message, it will take a while...')
  if message == '':
    while next_nothing != '-1':
      u = opener.open(startAddr + next_nothing)
      for cookie in cookie_jar:
        if cookie.name == 'info':
          if cookie.value == '+':
            message += '%20'
          else:
            message += cookie.value
      rData = u.read().decode()
      indx = rData.find(marker)
      if indx == -1:
        next_nothing = '-1'
      else:
        next_nothing = rData[indx+len(marker):]

  message = bz2.decompress(urllib.parse.unquote_to_bytes(message))
  print(message.decode())
  
  message = 'the flowers are on their way'
  
  XMLRPCserver = xmlrpc.client.Server(
    'http://www.pythonchallenge.com/pc/phonebook.php'
  )
  
  print('Calling...')
  phone = XMLRPCserver.phone('Leopold')
  print(phone)
  
  url = "http://www.pythonchallenge.com/pc/stuff/"
  url += phone.split('-')[1].lower() + '.php'
  
  o = urllib.request.build_opener()
  o.addheaders.append(('Cookie', 'info=' + urllib.parse.quote_plus(message)))
  
  response = o.open(url)
  
  rData = response.read().decode()
  
  idx1 = rData.find('<br><br>', rData.find('leopold.jpg')) + 8
  idx2 = rData.find('</font>')
  
  print(rData[idx1:idx2])
  resultAddr = 'http://www.pythonchallenge.com/pc/return/'
  resultAddr += 'balloons.html'
  
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
