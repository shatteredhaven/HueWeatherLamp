#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:         Hue Weather Lamp
#
# Details &
# instructions: http://www.shatteredhaven.com/2013/01/1387365-philips-hue-weather-lamp.html
#
# Author:       shatteredhaven
# 
# Created:      January 2013
# 
# Adapted from Kindle Weather Display by Matt Petroff and uses phue library: https://github.com/studioimaginaire/phue/
# 
#-------------------------------------------------------------------------------

#modify the file path to where you unzipped the phue library files. This is a work around if you have not installed the phue python module
import sys; sys.path.append("/CHANGE/TO/FILEPATH/OF/PHUE LIBRARY")

import urllib2
from xml.dom import minidom
import time

from phue import Bridge

#change to IP address of your Philips Hue Hub
b = Bridge('XXX.XXX.XXX.XXX')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Fetch data (change lat and lon to desired location)
weather_xml = urllib2.urlopen('http://graphical.weather.gov/xml/SOAP_server/ndfdSOAPclientByDay.php?whichClient=NDFDgenByDay&lat=42.9133&lon=-85.7053&format=24+hourly&numDays=4&Unit=e').read()
dom = minidom.parseString(weather_xml)

# Parse temperatures
xml_temperatures = dom.getElementsByTagName('temperature')
temp = [None]*4
for item in xml_temperatures:
    if item.getAttribute('type') == 'maximum':
        values = item.getElementsByTagName('value')
        for i in range(len(values)):
            temp[i] = int(values[i].firstChild.nodeValue)

# Parse precipitation
xml_precipitation = dom.getElementsByTagName('probability-of-precipitation')
chance = [None]*8
for item in xml_precipitation:
    if item.getAttribute('type') == '12 hour':
        values = item.getElementsByTagName('value')
        for i in range(len(values)):
            chance[i] = int(values[i].firstChild.nodeValue)

# turn the lamp on if it is not already
b.set_light(1,'on', True)

#read the temperature from yesterday
fin = open('temp.txt', 'r')
yday = fin.read()

# convert the string from the txt file to integer
ydaytemp = int(yday)

#
# perform a temperature check against yesterday's temp with today's
#

if ydaytemp > temp [0]:
# set lamp to blue for cooler weather
    b.set_light(1,'hue', 46668)

if ydaytemp < temp [0]:
# set lamp to red for cooler weather
    b.set_light(1,'hue', 836)

elif ydaytemp == temp [0]:
# set lamp to green for same weather
    b.set_light(1,'hue', 27117)

# check for precipitation.
# Turn lamp purple if chance of precipitation is greater than 70%
x=0
for x in range (0, 7):
    if chance [x] > 70:
        b.set_light(1,'hue', 51457)
        x=x+1

#delay for 1 hour then turn lamp off
time.sleep(3600)
b.set_light(1,'on', False)

#write today's temperature to txt file
hightemp = temp [0]
fout = open ('temp.txt', 'w')
fout.write(str(hightemp))
fout.seek(0)
