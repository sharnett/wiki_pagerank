from scipy.io import loadmat
from cPickle import load, dump
from numpy.linalg import norm
from numpy import ones, divide, argsort, array
from numpy import load as nload
from numpy import save as nsave
from scipy.sparse import coo_matrix
from itertools import islice, count
import os.path

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
	y = nload(open('A.npy'))
	print 'loaded A.npy'
	A = coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
	print 'created coo_matrix'
	d2s = load(open('dense_to_sparse.pickle'))
	print 'loaded dense_to_sparse.pickle'
	i2t = load(open('ID-title_dict.pickle'))
	print 'loaded ID-title_dict.pickle'
	return A, d2s, i2t

def top_k(k = 10, v = None):
	''' does all titles if k < 0 '''
	A, d2s, i2t = load_data()
	print 'data loaded and being read by top_k'
	if v is None:
		if os.path.isfile('pr.out.npy') == True: 
			print 'loading existing PR computation'
			v = nload('pr.out.npy')
			print 'loaded to memory'
		else:
			print 'doing pagerank'
			v = pagerank(A)
			print 'done computing PR, saving'
			nsave('pr.out.npy', v)
			print 'saved'
	print 'sorting'
	t = reversed(argsort(array(v)[:,0])) # pageranked list of dense IDs
	print 'getting titles'
	def get_title(x):
		''' convert dense ID to sparse ID, then sparse ID to title '''
		i = d2s[x]
		try:
			return i2t[i]
		except KeyError:
			return 'TITLE_ERROR'
	return (get_title(x) for x in islice(t, k)) if k >= 0 else (get_title(x) for x in t)

def main():
	for i, title in enumerate(top_k(), 1):
		print('%2d %s' % (i, title))

if __name__ == '__main__':
	main()
