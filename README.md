wiki_pagerank
=============

##Some results

* [top 100 english](https://gist.github.com/sharnett/8089331)
* [full english results](https://ia601006.us.archive.org/27/items/en_wikipedia_article_titles_by_pagerank_dated_20131202.txt/en_wikipedia_article_titles_by_pagerank.txt) (209 MB file)
* [top 100 tagalog](https://gist.github.com/sharnett/8089293)

Sorting Wikipedia article dumps by PageRank
-------------------------------------

Sean Harnett advises that you may want to try using Map Reduce on a
 cloud / distributed cluster to speed the creation of graph.txt for larger
 Wikipedia language versions, or just use a beefy computer and accept 
 it may take a while. But please test with a small Wikipedia first to
 ensure you have all the dependency like scipy.
Also an Solid State Disk drive may help.

I've adapted Sean's scripts so that all you should need to do is put 
the decompressed pagelinks.sql and page.sql files into this folder as
the working directory, then run test_getting_wikipedia_pageranks.sh

To test it, as I'm visiting family my girlfriends family in the Philippines,
I figured the Tagalog Wikipedia could be a good small test Wikipedia.
As of December 2013, tlwiki-latest-pagelinks.sql decompresses to 95 MB,
and tlwiki-latest-page.sql - the list of articles, expands to 16 MB.
I have included a file to download and extract this.

Example Usage
-------------------------------------

    sudo apt-get install python-scipy
    ./download_and_extract.sh
    python main.py

This should take a couple minutes and get you something like this:

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


-------------------------------------
Background by Luke Stanley

Realising that often bandwidth is bad, I got excited about offline
 Wikipedia collections.
I decided to give the gift of knowledge for Christmas (as well as some
 bootable Ubuntu for some relatives with virus ridden XP boxes).

But I was disappointed that a bunch of articles I thought were really
 important were missing from existing offline Wikipedia article collections.
 
They were out of date, and the manual selections of articles people 
chose was too limited in my opinion.
It wasn't clear if this was just distasteful choices or willful censorship.
So I thought the PageRank algorithm could be a good way to filter less
 significant articles, and make my own article collection instead of a
  presumably messy human bureaucracy for choosing what articles make the cut.
I found Sean Harnett had calculated PageRank before on Wikipedia dataset here: 
http://www.columbia.edu/~srh2144/neatthings/
I asked him to upload his Python scripts for doing so, and he kindly obliged
 putting them here on Github:
https://github.com/sharnett/wiki_pagerank

They didn't require much work to get going with a smaller Wikipedia dataset,
I wrote a few setup scripts for use on a single computer.
