#Ubuntu script, should work on r3.2xlarge with 200GB
sudo fallocate -l 50G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo apt-get update
sudo apt-get -y install git python-numpy build-essential cython python-scipy htop ncdu python-h5py pigz
git clone https://github.com/lukestanley/wiki_pagerank
cd wiki_pagerank/
echo "You may want to setup an alert trigger for when this instance has shut down"
echo "See aws_stats.png for CPU, network and disk usage"
wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz
pigz -dc *page.sql.gz > page.sql
echo "Extracted page.sql"
wget -c http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz
pigz -dc *pagelinks.sql.gz > pagelinks.sql
echo "Extracted pagelinks.sql"
python main.py .
echo "Compressing"
pigz --best -k pageranked.txt
echo "Done, shutting down"
sudo shutdown now
