from __future__ import print_function 
from os.path import isfile
from scipy.io import loadmat
from cPickle import load, dump
from numpy.linalg import norm
from numpy import ones, divide, argsort, array, load as nload, save as nsave
from scipy.sparse import coo_matrix
from itertools import islice, count


def pagerank(A, d=.85, tol=1e-3):
    n = A.shape[0]
    D = A.astype('i4').sum(1)
    D[D==0] = n
    At = A.transpose()
    v = ones((n,1))/n
    for i in count(1):
        prev = v
        v = d*(At*divide(v, D)) + (1-d)/n
        err = norm(v-prev)
        print('i =', i, 'err =', err)
        if err < tol:
            break
    return v

def load_data():
    print('loading data...')
    y = nload(open('A.npy'))
    print('loaded A.npy')
    A = coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
    print('created coo_matrix')
    d2s = load(open('dense_to_sparse.pickle'))
    print('loaded dense_to_sparse.pickle')
    i2t = load(open('ID-title_dict.pickle'))
    print('loaded ID-title_dict.pickle')
    return A, d2s, i2t

def top_k(k=10, v=None):
    ''' Returns top-k titles by PageRank. Uses previous PageRank computation v if provided.
        Does all titles if k < 0 '''
    A, d2s, i2t = load_data()
    print('data loaded and being read by top_k')
    if v is None:
        print('doing pagerank...')
        v = pagerank(A)
        print('done computing pagerank, saving...', end=' ')
        nsave('pr.out.npy', v)
        print('saved')
    print('sorting...')
    t = reversed(argsort(array(v)[:, 0]))  # pageranked list of dense IDs

    print('getting titles...')
    def get_title(x):
        ''' convert dense ID to sparse ID, then sparse ID to title '''
        i = d2s[x]
        try:
            return i2t[i]
        except KeyError:
            return 'TITLE_ERROR'
    return (get_title(x) for x in islice(t, k)) if k >= 0 else (get_title(x) for x in t)

def main():
    v = None
    if isfile('pr.out.npy'):
        print('loading existing pagerank computation from pr.out.npy...', end=' ')
        v = nload('pr.out.npy')
        print('loaded')
    for i, title in enumerate(top_k(v=v), 1):
        print('%2d %s' % (i, title))

if __name__ == '__main__':
    main()
