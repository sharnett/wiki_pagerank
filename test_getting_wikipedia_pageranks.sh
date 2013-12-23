#./download_and_extract_tagalog_wikipedia_dump.sh
rm *.pyc
rm *.mat
rm *.pickle
rm *.wc
rm graph.txt
cat page.sql | python make_title-ID_dict.py
cat pagelinks.sql | python make_graph_mapper.py | sort | python make_graph_reducer.py > graph.txt
python create_compact_dicts.py
python make_ID-title_dict.py
python compactify_graph.py
python pagerank.py
