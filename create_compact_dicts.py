from cPickle import dump
sparse_to_dense = {}
dense_to_sparse = []
for i, line in enumerate(open('graph.txt')):
    ID = int(line.split()[0])
    sparse_to_dense[ID] = i
    dense_to_sparse.append(ID)
    if i%100000 == 0: print i
dump(sparse_to_dense, open('sparse_to_dense.pickle', 'w'), 2)
dump(dense_to_sparse, open('dense_to_sparse.pickle', 'w'), 2)
