#!/usr/bin/env python

'''
:Note:
    - ElementTree.tostring() returns string in binary format
      so you cannot read it as a string, unless surrounded by
      str()
      
      TODO: no strings, use lxml library to modify nodes
'''


# Global Python imports and then add the configuration file import for 
# directory paths.
import os, sys, traceback, logging
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import config, wsgi_parser
from lxml import etree as ElementTree

logging.basicConfig(filename='/var/log/easywsgi/example.log', filemode='w',
                   level=logging.DEBUG)

def application(environ, start_response):

    name = environ.get('REQUEST_URI').lstrip('/')
    if not name:
        name = config.WEB_ENTRY_POINT
    path = os.path.join(config.WEB_FOLDER, name)
    page = open(path).read()
    
    
    if config.USE_TEMPLATES:
        # Read in Html File:
        # Call wsgi_parser.parse(string) to modify components based on config
        pass
    
    xml = bytes(page if page else wsgi_parser.load_error_page(config.ERRORS.get('404'),
                                                path), encoding="UTF-8")
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(xml)))]
    start_response(status, response_headers)
    yield xml