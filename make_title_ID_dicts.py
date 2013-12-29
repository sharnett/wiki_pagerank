#!/usr/bin/python
from re import finditer
from cPickle import dump

def process_line(line, d):
    ''' gets the ID and name for each page in the line '''
    pattern = "\((\d+),(\d+),'(.*?)','"
    for match in finditer(pattern, line):
        ID, namespace, name = match.groups()
        if namespace == '0': 
            d[name] = int(ID)

def main(infile = 'page.sql'):
    ''' Reads page.sql line by line and processes it '''
    print 'making title <--> ID dictionaries...'
    crap = 'INSERT INTO `page` VALUES'
    t2id = {}
    for line in open(infile):
        if line[:len(crap)] == crap: 
            process_line(line, t2id)
    id2t = {v:k for k, v in t2id.iteritems()}
    dump(t2id, open('title-ID_dict.pickle', 'w'), 2)
    dump(id2t, open('ID-title_dict.pickle', 'w'), 2)

if __name__ == "__main__":
    main()
