#!/bin/python

import httplib
import sys

def check_webserver(address, port, resource):
    ''' create a Http socket '''
    if not resource.startswith('/'):
        resource = '/' + resource
        
    try:
        conn = httplib.HTTPConnection(address, port)
        print 'HTTP connection created sucessfully'
        # make request
        req = conn.request('GTE', resource)
        print 'request for {resource} successful'.format(resource=resource)
        # get response
        response = conn.getresponse()
        print 'response status: {}'.format(response.status)

    except sock.error, e:
        print "HTTP connection failed: {}".format(e)
        return False
    finally:
        # be a good citizen and close your connection
        conn.close()
        print "Close the connection"
    if response.status in ['200', '301']:
        print 'Success - status was {}'.format(response.status)
        return True
    else:
        print 'Status was {}'.format(response.status)
        return False
        
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", default="localhost", help="ADDRESS for webserver", metavar="ADDRESS")
    parser.add_option("-p","--port",dest="port",type="int",default=80,help="PORT for webserver",metavar="PORT")
    parser.add_option("-r", "--resource", dest="resource", default="index.html",help="RESOURCE to check", metavar="RESOURCE")
    (options, args) = parser.parse_args()
    print 'options: {}, args: {}'.format(options, args)
    check = check_webserver(options.address,options.port,options.resource)
    print 'check the server return {}'.format(check)
    sys.exit(not check) 
    