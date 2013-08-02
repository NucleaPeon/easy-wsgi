#!/usr/bin/env python

# Global Python imports and then add the configuration file import for 
# directory paths.
import os, traceback, config
import wsgi_parser as wsgiparser

def application(environ, start_response):

    try:
        output = wsgiparser.parse_wsgi_tags(
            open(config.WEB_ENTRY_POINT).read()) # usually index.html
    except Exception as E:
        tb = traceback.format_exc()
        output="<html><head></head><body>Error: {}<br />{}<br /></body></html>".format(str(E), tb)
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    yield output
