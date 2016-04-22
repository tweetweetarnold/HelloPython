'''
Created on Apr 23, 2016

@author: Arnold
'''
import requests


if __name__ == '__main__':
    pass

print "Hello"

name = "Arnold"
age = 24
gender = 'M'

print name
print age
print gender

r = requests.get('https://api.github.com/events')
print r.json
print r.url

print "Done"
