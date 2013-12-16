#!/usr/bin/python
from sys import stdin
from re import finditer
from cPickle import dump

def process_line(line, d):
    ''' Prints the ID and name for each page in the line '''
    pattern = "\((\d+),(\d+),'(.*?)','"
    for match in finditer(pattern, line):
        ID, namespace, name = match.groups()
        if namespace == '0': 
            print ID, name
            d[name] = ID

def main():
    ''' Reads stdin line by line and processes it. Feed it the
    enwiki-YYYYMMDD-page.sql file'''
    crap = 'INSERT INTO `page` VALUES'
    d = {}
    for line in stdin:
        if line[:len(crap)] == crap: 
            process_line(line, d)
    dump(d, open('title-ID_dict.pickle', 'w'), 2)

if __name__ == "__main__":
    main()
