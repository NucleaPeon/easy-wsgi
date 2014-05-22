#!/usr/bin/env python

# Global Python imports and then add the configuration file import for 
# directory paths.
import os, sys, traceback
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import config

def application(environ, start_response):

    try:
        #if config.USE_TEMPLATES:
            #html = wsgi_parser.Html()
        #else:
            #html = wsgi_parser.Html(htmlfile=config.WEB_ENTRY_POINT)
        #asdf = open('/tmp/wsgi', 'w')
        #asdf.write(str(html))
        #asdf.close()
        output = b"""<b>Hello World</b>"""
    except Exception as E:
        tb = traceback.format_exc()
        output="<html><head></head><body>Error: {}<br />{}<br /></body></html>".format(str(E), tb)
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    yield output

'''
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"Hello World!"]
'''