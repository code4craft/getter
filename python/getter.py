#! /usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'yihua'
import optparse
import os
import re
import fileinput

filename = os.path.expanduser('~') + "/.getrc"


class Getter():
    data = {}

    def __init__(self):
        matcher = re.compile(r"(.*?)\s+(.*)")
        for line in fileinput.input(filename):
            r = matcher.match(line)
            if r:
                self.data[r.group(1)] = r.group(2)
        pass


    def process(self, args):
        if len(args) == 0:
            print  open(filename).read()
        try:
            if self.data[args[0]]:
                print self.data[args[0]]
        except:
            pass


pass

if __name__ == '__main__':
    parser = optparse.OptionParser()
    options, args = parser.parse_args()
    getter = Getter()
    getter.process(args)