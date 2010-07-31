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
    #page = wget(url)
    page = open('data.html').read()

    doc = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
    if doc:
        iconf = doc.findAll('pre')
        my_iconf = BeautifulStoneSoup(iconf[0].string)

        return my_iconf


conference = pull_conference(indico_url)
#print conference


for session in conference.findAll('session'):
    print "*-------------------------------------------------------------"
    print session
    print "ID:         " + session.id.contents[0]
    print "code:       " + session.code.contents[0]
    print "Title       " + session.title.contents[0]
    if session.convener:
        print "Convener:   " + session.convener.contents[0]

    print "*---------------------"
    print session.convener
    print "*---------------------"


#    if session.user and session.user.title:
#        print "User title: " + session.user.title[0]
    if session.user:
        if session.user.title.string:
            print "Title        :  " + session.user.title.string
        if session.user.name:
            print "Name         :  " + session.user.name
        if session.user.organization.string:
            print "Organization :  " + session.user.organization.string
        if session.user.email.string:
            print "Email        :  " + session.user.email.string
#    if session.user and session.user.email:
    print session.user

#    if session.user and session.user.email:
#        print "User email: " + session.user.email[0]
    #print session.location
    #print "Location name: " + session.location.name.string
    #print session.location.room
    #print "Location addr: " + session.location.address.string
    print "Location room: " + session.location.room.string
    print "Start time   : " + session.startdate.string
    print "Stop time    : " + session.enddate.string
    if session.description.string:
        print "Description  : " + session.description.string


#    print "**----"


    #for i in session:
        #print "**---"
        #print i


