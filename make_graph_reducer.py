#!/usr/bin/python
from sys import stdin
from re import finditer
from cPickle import load

def main():
    ''' 
    '''
    current_page, current_list = None, []
    for line in stdin:
        x = line.split()
        from_page, to_pages = x[0], x[1:]
        if from_page != current_page:
            if current_page: print current_page, ' '.join(current_list)
            current_page, current_list = from_page, []
        current_list += to_pages
    print current_page, ' '.join(current_list)

if __name__ == "__main__":
    main()
