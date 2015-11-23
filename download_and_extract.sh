wget http://dumps.wikimedia.org/tlwiki/latest/tlwiki-latest-page.sql.gz -O data/tl_page.sql.gz
wget http://dumps.wikimedia.org/tlwiki/latest/tlwiki-latest-pagelinks.sql.gz -O data/tl_pagelinks.sql.gz
#wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz -O data/en_pagelinks.sql.gz
#wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz -O data/en_pagelinks.sql.gz
gunzip -c data/*page.sql.gz > data/page.sql
gunzip -c data/*pagelinks.sql.gz > data/pagelinks.sql
