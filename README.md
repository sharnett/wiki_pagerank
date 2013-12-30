#wiki_pagerank

This is a set of python scripts to run PageRank on the wikipedia link graph. 

##Background by Luke Stanley

Realising that often bandwidth is bad, I got excited about offline Wikipedia
collections.  I decided to give the gift of knowledge for Christmas (as well as
some bootable Ubuntu for some relatives with virus ridden XP boxes).

But I was disappointed that a bunch of articles I thought were really important
were missing from existing offline Wikipedia article collections. They were out
of date, and the manual selections of articles people chose was too limited in
my opinion.  It wasn't clear if this was just distasteful choices or willful
censorship.

I thought the PageRank algorithm could be a good way to filter less significant
articles, and make my own article collection instead of a presumably messy
human bureaucracy for choosing what articles make the cut.  I found Sean
Harnett had calculated PageRank before on Wikipedia dataset here:
http://www.columbia.edu/~srh2144/neatthings/ I asked him to upload his Python
scripts for doing so, and he kindly obliged putting them here on Github:
https://github.com/sharnett/wiki_pagerank

They didn't require much work to get going with a smaller Wikipedia dataset, I
wrote a few setup scripts for use on a single computer.

##Some results

* [top 100 english](https://gist.github.com/sharnett/8089331)
* [full english results](https://ia601006.us.archive.org/27/items/en_wikipedia_article_titles_by_pagerank_dated_20131202.txt/en_wikipedia_article_titles_by_pagerank.txt) (209 MB file)
* [top 100 tagalog](https://gist.github.com/sharnett/8089293)
* [analysis of inlink and outlink distributions](http://nbviewer.ipython.org/github/sharnett/wiki_pagerank/blob/master/tagalog%20inlink%20and%20outlink%20distributions.ipynb) for tagalog wikipedia

##Example Usage

    sudo apt-get install python-scipy
    ./download_and_extract.sh
    python main.py

This should take a minute or so and get you something like this:

    making title <--> ID dictionaries...
    building the graph...
    compactifying...
    reading graph file and matrixifying...
    loading data...
    doing pagerank
    i = 1 err = 0.0721205984186
    i = 2 err = 0.0309899557399
    i = 3 err = 0.0180857631125
    i = 4 err = 0.00638996682224
    i = 5 err = 0.00302626819411
    i = 6 err = 0.00118320972815
    i = 7 err = 0.000542479457445
    sorting
     1 Wikipedia
     2 Malayang_software
     3 Wikang_Ingles
     4 Malayang_sopwer
     5 Hapon
     6 Estados_Unidos
     7 Pilipinas
     8 Ensiklopedya
     9 GNU/Linux
    10 World_Wide_Web

##Tips

You may want to use MapReduce to speed the creation of graph.txt for
larger Wikipedia language versions (the original motivation was an excuse to
play with MapReduce). Included are the mapper and reducer scripts if you want
to go that route. In any case, you should definitely test with a small
Wikipedia first to ensure that things work properly.

Luke ended up needing to use a big EC2 instance to run it on the full English
wikipedia as his laptop didn't have enough memory.

The Tagalog Wikipedia is a good small test Wikipedia.  As of December 2013,
tlwiki-latest-pagelinks.sql decompresses to 95 MB, and tlwiki-latest-page.sql --
the list of articles -- expands to 16 MB.  Included is a file to download and
extract these.
