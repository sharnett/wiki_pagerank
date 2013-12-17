wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz
gunzip -c *page.sql.gz > page.sql
wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz
gunzip -c *pagelinks.sql.gz > pagelinks.sql
