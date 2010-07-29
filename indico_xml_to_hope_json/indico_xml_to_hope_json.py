#!/usr/bin/env python

import sys
import urllib2
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


indico_url = "https://www.egi.eu/indico/conferenceOtherViews.py?confId=48&view=xml&showDate=all&showSession=all&detailLevel=contribution"


def wget(url):
    request = urllib2.Request(url)

    try:
        sock = urllib2.urlopen(request)
        if sock:
            data = sock.read()
            sock.close()

        return data
    except Exception, e:
        print "wget %s" % e
        return


def pull_conference(url):
    page = wget(url)

    doc = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
    if doc:
        # print doc

        iconf = doc.findAll('pre')
        my_iconf = BeautifulStoneSoup(iconf[0].string)

        return my_iconf


conference = pull_conference(indico_url)
#print conference


for session in conference.findAll('session'):
    print "*----"
    #print session
    print session.id
    print session.id.contents
    print session.id.contents[0]

    #for i in session:
        #print "**---"
        #print i


