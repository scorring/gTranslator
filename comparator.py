#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, collections, time
from pprint import pprint
import config

cfg_nb = {"nb_words_1": 0, "nb_words_2": 0}



def printNumberOfWords(obj, clef):
    for key, value in obj.iteritems():
        if isinstance(value, dict):
            printNumberOfWords(value, clef)
        else:
            cfg_nb[clef] += 1

keys = ([], [])

def compare(data_1, data_2):
    def extractkey(obj, data_idx, ancestors=[]):
        for idx, (key, value) in enumerate(obj.iteritems()):
            c_ancestors = list(ancestors)
            if isinstance(value, dict):
                c_ancestors.append(key)
                extractkey(value, data_idx, c_ancestors)
            else:
                if (len(c_ancestors)):
                    keys[data_idx].append('.'.join(c_ancestors) + '.' + key)
                else:
                    keys[data_idx].append(key)


    datas = (data_1, data_2)
    for data_idx, data in enumerate(datas):
        extractkey(data, data_idx)

    return (list(set(keys[0]) - set(keys[1])), list(set(keys[1]) - set(keys[0])))


with open(config.first_file_to_compare_1) as first_file_to_compare_1:
    data_1 = json.load(first_file_to_compare_1, object_pairs_hook=collections.OrderedDict)
    with open(config.first_file_to_compare_2) as first_file_to_compare_2:
        data_2 = json.load(first_file_to_compare_2, object_pairs_hook=collections.OrderedDict)
        printNumberOfWords(data_1, 'nb_words_1')
        printNumberOfWords(data_2, 'nb_words_2')
        keys1not2, keys2not1 = compare(data_1, data_2)
        print "Number of words in %s: %s" % (config.first_file_to_compare_1, cfg_nb['nb_words_1'])
        print "Number of words in %s: %s" % (config.first_file_to_compare_2, cfg_nb['nb_words_2'])
        print "Clefs présentes dans %s et non dans %s :" % (config.first_file_to_compare_1, config.first_file_to_compare_2)
        pprint(keys1not2)
        print ""
        print "Clefs présentes dans %s et non dans %s :" % (config.first_file_to_compare_2, config.first_file_to_compare_1)
        pprint(keys2not1)
