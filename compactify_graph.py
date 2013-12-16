from cPickle import load
from scipy.io import savemat
from scipy.sparse import lil_matrix, csr_matrix

def create_matrix(n = 0, test=True, A=None, sparse_to_dense=None):
    #n = 26956134
    n = 10807612
    if not sparse_to_dense:
        print 'loading conversion dictionary...'
        sparse_to_dense = load(open('sparse_to_dense.pickle'))
    if not A:
        print 'allocating matrix...'
        A = lil_matrix((n,n), dtype='i1')
    graph_file = 'graph_test.txt' if test else 'graph.txt' 
    print 'reading graph file...'
    for k, line in enumerate(open(graph_file)):
        converted = [sparse_to_dense.get(int(ID), -1) for ID in line.split()]
        i = converted[0]
        for j in converted[1:]:
            if j>=0: A[i, j] = 1
        if k%100000 == 0: print k
    return A

if __name__ == '__main__':
    A = create_matrix(test=False)
    dump('A', {'A': A})
