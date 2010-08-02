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
    #print session
    print "ID                     : " + session.id.contents[0]
    print "code                   : " + session.code.contents[0]
    print "Title                  : " + session.title.contents[0]

    if session.convener:
#        print "len(session.convener) " + str(len(session.convener))
        for user_tag in session.convener.findAll('user'):
            print user_tag.__class__
            print user_tag.__class__.__name__
            for user_tag_content in user_tag:
                print "**---"
                print user_tag_content.__class__
                print user_tag_content.__class__.__name__
                print user_tag_content
                print "**---"

            # print users.string

#        print session.convener.__class__
#        for conv in session.convener:
#            print conv.__class__
#            print "len(conv) " + str(len(conv))
#            for c in conv:
#                print c.__class__
#                print "foo"
#                for i in c:
#                    print i


        #print len(session.convener.user)

    if session.convener and session.convener.user:
        if session.convener.user.title and session.convener.user.title.string:
            print "Convener title         : " + session.convener.user.title.string
        if session.convener.user.organization and session.convener.user.organization.string:
            print "Convener organization  : " + session.convener.user.organization.string
        if session.convener.user.email and session.convener.user.email.string:
            print "Convener email         : " + session.convener.user.email.contents[0]

        #for userinfo in session.convener.user.contents:
        #    print "---"
        #    print userinfo

        #    for u in userinfo:
        #        print u

            #if userinfo and userinfo.string:
            #    print "Convener some user     : " + str(userinfo) + " " + userinfo.string
#            print userinfo.organization
        #    print "---"



    if session.location:
        if session.location.room and session.location.room.string:
            print "Location room          : " + session.location.room.string
        if session.location.address and session.location.address.string:
            print "Location addr          : " + session.location.address.string

    print "Start time             : " + session.startdate.string
    print "Stop time              : " + session.enddate.string
    #if session.description.string:
    #    print "Description  : " + session.description.string


    print "*---------------------"
    print session.convener
    print "*--"
    if session.convener and session.convener.user:
        print session.convener.user
    print "*--"
    print session.location
    print "*---------------------"



    #print session.location
    #print "Location name: " + session.location.name.string
    #print session.location.room
    #print "Location addr: " + session.location.address.string


