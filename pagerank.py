from scipy.io import loadmat
from cPickle import load
from numpy.linalg import norm
from numpy import ones, divide, argsort, array
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
        print 'i =', i, 'err =', err
        if err < tol:
            break
    return v

def load_data():
    print 'loading data...'
    A = loadmat('A.mat')['A']
    d2s = load(open('dense_to_sparse.pickle'))
    i2t = load(open('ID-title_dict.pickle'))
    return A, d2s, i2t

def top_k(k = 10, v = None):
    A, d2s, i2t = load_data()
    if v is None:
        print 'doing pagerank'
        v = pagerank(A)
    print 'sorting'
    t = reversed(argsort(array(v)[:,0])) # pageranked list of dense IDs
    def get_title(x):
        ''' convert dense ID to sparse ID, then sparse ID to title '''
        i = d2s[x]
        return i2t[i]
        #return i2t[str(i)]
    return [get_title(x) for x in islice(t, k)]

if __name__ == '__main__':
    for i, title in enumerate(top_k(), 1):
        print('%2d %s' % (i, title))
