from cPickle import load, dump
from scipy.io import savemat
from scipy.sparse import coo_matrix

def create_compact_dicts():
    print 'compactifying...'
    sparse_to_dense, dense_to_sparse = {}, []
    for i, line in enumerate(open('graph.txt')):
        ID = int(line.split()[0])
        sparse_to_dense[ID] = i
        dense_to_sparse.append(ID)
    dump(sparse_to_dense, open('sparse_to_dense.pickle', 'w'), 2)
    dump(dense_to_sparse, open('dense_to_sparse.pickle', 'w'), 2)

def create_matrix():
    sparse_to_dense = load(open('sparse_to_dense.pickle'))
    print 'reading graph file and matrixifying...'
    I, J = [], []
    for line in open('graph.txt'):
        converted = [sparse_to_dense.get(int(ID), -1) for ID in line.split()]
        converted = [x for x in converted if x>=0]
        i = converted[0]
        I.extend([i]*(len(converted)-1))
        J.extend(converted[1:])
    n = max([max(I), max(J)]) + 1
    data = [1]*len(I)
    return coo_matrix((data, (I,J)), shape=(n,n), dtype='i1')

if __name__ == '__main__':
    create_compact_dicts()
    A = create_matrix()
    savemat('A', {'A': A})
