import make_title_ID_dicts
import make_graph
import compactify
import pagerank
from sys import argv

def test():
    ''' does everything, prints top 10 results. needs page.sql and pagelinks.sql 
    files which can be downloaded using download_and_extract.sh '''
    make_title_ID_dicts.main()
    make_graph.main()
    compactify.main()
    pagerank.main()

def actual(outfile='pageranked.txt'):
    ''' does everything and writes all results to file '''
    make_title_ID_dicts.main()
    make_graph.main()
    compactify.main()
    with open(outfile, 'w') as f:
        for page in pagerank.top_k(-1):
            f.write(page + '\n')

if __name__ == '__main__':
    test() if len(argv) == 1 else actual()
