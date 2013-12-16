from scipy.io import loadmat
from numpy import argsort, array
from pagerank import pagerank
from cPickle import load

def top_k(k = 10, A = None, v = None, d2s = None, i2t = None):
    if v is None:
        if A is None:
            print 'loading A'
            A = loadmat('/home/sean/wiki_data/A.mat')['A']
        print 'doing pagerank'
        v = pagerank(A)
    if not d2s:
        print 'loading denseID to sparseID dictionary'
        d2s = load(open('/home/sean/wiki_data/dense_to_sparse.pickle'))
    if not i2t:
        print 'loading ID to title dictionary'
        i2t = load(open('/home/sean/wiki_data/ID-title_dict.pickle'))
    print 'sorting'
    t = argsort(array(v)[:,0])
    m = t[-1:-(k+1):-1]
    answer = []
    for x in m:
        #i = d2s.get(x)
        i = d2s[x]
        print i
        title = i2t.get(i) if i is not None else 'd2s error'
        if not title:
            title = 'i2t error'
        answer.append(title)
    return answer    
