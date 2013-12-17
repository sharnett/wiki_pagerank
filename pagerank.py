from scipy.sparse import spdiags
from numpy.linalg import norm
from numpy import ones, divide

#def pagerank(M, d=.85, tol=1e-3):
def pagerank(A, d=.85, tol=1e-3):
    n = A.shape[0]
    D = A.astype('i4').sum(1)
    D[D==0] = n
    At = A.transpose()
    v = ones((n,1))/n
    err = tol+1
    i = 1
    print 'i =', i, 'err =', err
    while err > tol:
        prev = v
        v = d*(At*divide(v, D)) + (1-d)/n
        err = norm(v-prev)
        i += 1
        print 'i =', i, 'err =', err
    return v

def create_M(A):
    ''' Not worth it. Better to use A directly '''
    n = A.shape[0]
    At = A.transpose()
    x = At.astype('i4').sum(0)
    x[x==0] = n
    D = spdiags(1.0/x, 0, n, n)
    return At*D
