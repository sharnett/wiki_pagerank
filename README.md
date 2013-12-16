wiki_pagerank
=============

Playing with the wikipedia link graph
-------------------------------------

download files pagelinks.sql and page.sql

***cat pagelinks.sql | make_graph_mapper.py | sort | make_graph_reducer.py > graph.txt

wc -l graph.txt

./create_compact_dicts.py

cat page.sql | make_title-ID_dict.py

./make_ID-title_dict.py

set n to value from wc above

**./compactify_graph

ipython

top_k


** - takes maybe 20 minutes?

*** - takes a really long time. might actually require mapreduce.


  501  cat ../enwiki-20080103-pagelinks.sql | ./make_graph_mapper.py | sort | ./make_graph_reducer.py > graph.txt
  502  ls
  503  rm *pickle
  504  vi create_compact_dicts.py 
  505  ./create_compact_dicts.py 
  506  ls ..
  507  cat ../enwiki-20080103-page.sql | ./make_title-ID_dict.py 
  508  ./make_ID-title_dict.py
  509  wc -l graph.txt
  510  ls
  511  ipython
  512  vi compactify_graph.py 
  513  vi compactify_graph.py 
  514  ./compactify_graph.py 
  515  ls
  516  ipython

