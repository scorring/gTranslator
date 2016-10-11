#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, collections, time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import config

chromedriver = config.chromedriver_path
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

file = open(config.out_path, "w")

cfg_nb = {"nb_words": 0, "nb_left": 0}

def printNumberOfWords(obj):
    for key, value in obj.iteritems():
        if isinstance(value, dict):
            printNumberOfWords(value)
        else:
            cfg_nb['nb_words'] += 1


def introspect(obj, nb_tabs, file):
    for idx, (key, value) in enumerate(obj.iteritems()):
        # s = '\t"%s": ' % key
        s = '%s"%s": ' % (nb_tabs * '\t', key.encode('utf-8'))
        if isinstance(value, dict):
            s += '{\n'
            nb_tabs = nb_tabs + 1
            file.write(s)
            introspect(value, nb_tabs, file)
            nb_tabs = nb_tabs - 1
            if idx == len(obj) - 1:
                file.write('%s}\n' % (nb_tabs * '\t'))
            else:
                file.write('%s},\n' % (nb_tabs * '\t'))
        else:
            utf8Value = value.encode('utf-8')
            driver.get("https://translate.google.fr/#%s/%s/%s" % (config.in_language_code, config.out_language_code, utf8Value))
            time.sleep(1)
            result = driver.find_element_by_id('result_box').text.encode('utf-8')
            cfg_nb['nb_left'] -= 1
            print "%s -> %s" % (utf8Value, result)
            print "%s words remaining..." % cfg_nb['nb_left']
            if idx == len(obj) - 1:
                s += '"%s"\n' % result.replace('"', '\\"')
            else:
                s += '"%s",\n' % result.replace('"', '\\"')

            file.write(s)

        # else:
        #     print value.encode('utf-8')

with open(config.in_path) as data_file:
# with open('en.json') as data_file:
    file.write('{\n')
    data = json.load(data_file, object_pairs_hook=collections.OrderedDict)
    printNumberOfWords(data)
    print "Number of words to translate: %s" % cfg_nb['nb_words']
    cfg_nb['nb_left'] = cfg_nb['nb_words']
    introspect(data, 1, file)
    file.write('}\n')
    driver.close()
    file.close()
