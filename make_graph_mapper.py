#!/usr/bin/python
from sys import stdin
from re import finditer
from cPickle import load

def process_line(line, d):
    ''' 
    Prints outlinks for each page.

    Example contents of line: 
    ...'),(12,0,'A._S._Neill'),(12,0,'AK_Press'),(12,0,...

    Each tuple is of the form ('from' page, namespace, 'to' page).  Print a
    line for each 'from' page with the outlinks that are in namespace 0 (the
    main wikipedia, ignores 'talk' pages, etc). Annoyingly, the 'from' pages
    are given by ID and the 'to' pages by name. Use the dictionary d to map the
    text names to IDs for consistency (and some space savings).  
    '''
    pattern = "\((\d+),(\d+),'(.*?)'\)[,;]"
    current_page = None
    for match in finditer(pattern, line):
        from_page, namespace, to_page = match.groups()
        if from_page != current_page: 
            if current_page: print '' # new line for all but the first
            print from_page,
            current_page = from_page
        if namespace == '0' and to_page in d: print d[to_page],

def main():
    ''' Reads stdin line by line and processes it. Feed it the
    enwiki-YYYYMMDD-pagelinks.sql file. Needs the pickled dictionary mapping
    page names to IDs '''
    crap = 'INSERT INTO `pagelinks` VALUES'
    path = ''#set if needed (different current dir)
    pickle = 'title-ID_dict.pickle'
    d = load(open(path+pickle))
    for line in stdin:
        if line[:len(crap)] == crap: 
            process_line(line, d)

if __name__ == "__main__":
    main()
