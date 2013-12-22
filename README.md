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
    ./download_and_extract_tagalog_wikipedia_dump.sh
    ./test_getting_wikipedia_pageranks.sh

This should take a couple minutes and get you something like this:

    loading conversion dictionary...
    allocating matrix...
    reading graph file...
    loading A
    doing pagerank
    i = 1 err = 1.001
    i = 2 err = 0.0721206085496
    i = 3 err = 0.0309899616446
    i = 4 err = 0.0180857531626
    i = 5 err = 0.00638996220934
    i = 6 err = 0.0030262687189
    i = 7 err = 0.00118320968906
    i = 8 err = 0.000542479816184
    loading denseID to sparseID dictionary
    loading ID to title dictionary
    sorting
    Wikipedia
    Malayang_software
    Wikang_Ingles
    Malayang_sopwer
    Hapon
    Estados_Unidos
    Pilipinas
    Ensiklopedya
    GNU/Linux
    World_Wide_Web

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
