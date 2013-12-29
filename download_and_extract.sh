wget http://dumps.wikimedia.org/tlwiki/latest/tlwiki-latest-page.sql.gz
#wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz
gunzip -c *page.sql.gz > page.sql
wget http://dumps.wikimedia.org/tlwiki/latest/tlwiki-latest-pagelinks.sql.gz
#wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz
gunzip -c *pagelinks.sql.gz > pagelinks.sql
