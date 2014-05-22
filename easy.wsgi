#!/usr/bin/env python

# Global Python imports and then add the configuration file import for 
# directory paths.
import os, sys, traceback, logging
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import config

logging.basicConfig(filename='/var/log/easywsgi/example.log', filemode='a',
                   level=logging.DEBUG)

def application(environ, start_response):

    try:
        if config.USE_TEMPLATES:
            # Read in Html File:
            logging.debug("Using Templates")
        
        output = ['''<b>Hello World</b>''']
        output.append('''This is a new line in code, but only a <br /> does a new line in html''')
        
    except Exception as E:
        tb = traceback.format_exc()
        output="<html><head></head><body>Error: {}<br />{}<br /></body></html>".format(str(E), tb)
        
    # Break down organized html code into one byte string:
    output = bytes('\n'.join(output), encoding="UTF-8")
    
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