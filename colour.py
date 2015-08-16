__author__ = 'chris'
from html import HTML
import subprocess
import xml.etree.ElementTree as ET

tree = ET.parse('/home/chris/scripts/test.xml')
root = tree.getroot()

H = HTML('html')

H.h1("Speed in milliseconds")

rrd_dump = subprocess.check_output(
    ["rrdtool", "dump", "test.rrd", "test.xml"])

for ds in root.findall('ds'):
    #	name = ds.find('name').text
    last = ds.find('last_ds').text

ms = int(last)


def colour(x):
    if x < 2000:
        return ('green')
    else:
        return ('red')


fontc = colour(ms)

# unable to escape the - from http-equiv
dct = {
    'http-equiv': 'refresh', 'content': '5'
}

H.meta(**dct)
H.font(size="50", color="%s" % (fontc), face="arial")(("%s m/s") % (last))
H.p('Current ping to live.sipgate.co.uk - green:good | red:bad')

value = str(H)

html = open("colour.html", "w")
html.write(value)
html.close()
