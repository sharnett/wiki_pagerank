#./download_and_extract_tagalog_wikipedia_dump.sh
rm *.pyc
rm *.mat
rm *.pickle
rm graph.txt
python make_title-ID_dicts.py
echo "building the graph..."
cat pagelinks.sql | python make_graph_mapper.py | sort | python make_graph_reducer.py > graph.txt
python compactify.py
python pagerank.py
