#!/bin/python3.4


import time
import configparser
import logging

# variable definitions
configFile = '../conf.d/angryNinja.ini'


conf = configparser.ConfigParser()
conf.read(configFile)

# printing sections
print(conf.sections())


try:
    for key in conf['Defaults']:
        print(key)
except ImportError:
    print("error as", e)
finally:
    print("program is executed")





