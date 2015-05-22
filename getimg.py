#!/usr/bin/python
# download images from text file containing urls to current working directory
# url must containing an image file name behind the last /
# e.g.
# http://www.website.com/header.jpg
# http://www.website.com/image2.gif
# written by
# stephan.rossbauer@gmail.com

import sys, os, urllib2


def url2file(url):
    # function to download image from url
    filename = url.split('/')[-1]
    try:
        resp = urllib2.urlopen(url).read()
        if(os.path.exists(filename)):
            print "ERROR filename already exists. Skipping url: "+url
        else:
            f = open(filename, 'w')
            f.write(resp)
            f.close()
    except urllib2.URLError, e:
        print "ERROR("+str(e.code)+") for url "+url

		
		
# get filename from first commandline argument
if len(sys.argv) >= 2:
    workfile = str(sys.argv[1])

    # catch errors with the commandline argument
    try:	
	    f = open(workfile, 'r')
	    for line in f:
    		line = line.rstrip()
	    	url2file(line)
	    f.close()
    except IOError as e:
        print("{}".format(e))
else:
    print "Usage: getimg.py inputfile.txt"