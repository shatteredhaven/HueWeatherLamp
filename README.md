HueWeatherLamp
==============

Philips Hue lamp controlled by python script to change colors depending on the weather


Overview of the Philips Hue Weather Lamp: 
A python script (using a phue library) reads temperature from NOAA, compares it to a text file that has yesterdays temperature saved, and adjusts the color accordingly. The colors are: 

- If the temperature for today is cooler than yesterday, the lamp will turn blue
- If the temperature for today is warmer than yestrerday, the lamp will turn red
- If the temperature for today is the same as yesterday, the lamp will turn green
- If there is a 70% or higher chance of precipitation the lamp will be purple, regardless of a temperature increase or decrease.

Additional information and photos can be found here: http://www.shatteredhaven.com/2013/01/1387365-philips-hue-weather-lamp.html

Requirements: 
- Hue Lamps: http://www.meethue.com/en-US
- python (this program is written in 2.7): http://www.python.org/download/
- Philips Hue python library: https://github.com/studioimaginaire/phue
- computer capable of running cron or similar job scheduling function (ex. schtasks in Windows) 

Contents: 
- HueWeatherLamp.py - python script for weather lamp
- temp.txt - text file python writes the current day's temperature to
- weatherball - cron job example

Installation: 
A more detailed description of this project can be found here: http://www.shatteredhaven.com/2013/01/1387365-philips-hue-weather-lamp.html

Distribution: 
feel free to copy/modify/change/distribute at will! 
