from cPickle import load, dump
from scipy.io import savemat
from scipy.sparse import lil_matrix, csr_matrix

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
    for n,_ in enumerate(open('graph.txt'), 1):
        pass
    sparse_to_dense = load(open('sparse_to_dense.pickle'))
    A = lil_matrix((n,n), dtype='i1')
    graph_file = 'graph.txt' 
    print 'reading graph file and matrixifying...'
    for line in open(graph_file):
        converted = [sparse_to_dense.get(int(ID), -1) for ID in line.split()]
        i = converted[0]
        for j in converted[1:]:
            if j>=0: A[i, j] = 1
    return A

if __name__ == '__main__':
    create_compact_dicts()
    A = create_matrix()
    savemat('A', {'A': A})
