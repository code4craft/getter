#! /usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'yihua'
import optparse
import os
import re
import fileinput


class Adder():
    data = {}

    def __init__(self):
        matcher = re.compile(r"(.*?)\s+(.*)")
        for line in fileinput.input(os.path.expanduser('~') + "/.getrc"):
            r = matcher.match(line)
            if r:
                self.data[r.group(1)] = r.group(2)
        pass

    def process(self, args):
        if len(args) == 1:
            try:
                del self.data[args[0]]
            except:
                print "key '"+ args[0] + "' does not exist!"
            return

        self.data[args[0]] = args[1]
        self.save()

    def save(self):
        file = open(os.path.expanduser('~') + "/.getrc", "w")
        for d in self.data:
            file.write(d + "\t" + self.data[d] + "\n")
        file.close()


pass

if __name__ == '__main__':
    parser = optparse.OptionParser()
    options, args = parser.parse_args()
    if len(args) > 2 or len(args) < 1:
        print "Usage: add name [value]"
        exit(0)
    adder = Adder()
    adder.process(args)