#!/usr/bin/python
from cPickle import load, dump

def main():
    t2id = load(open('title-ID_dict.pickle'))
    id2t = {v:k for k, v in t2id.iteritems()}
    dump(d, open('ID-title_dict.pickle', 'w'), 2)

if __name__ == "__main__":
    main()
