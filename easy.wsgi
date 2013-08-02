#!/usr/bin/env python

# Global Python imports and then add the configuration file import for 
# directory paths.
import imp, os, re, sys, traceback, easy.conf

# IMPORTANT!
# ONLY SET PATHS IN SCRIPT load_env.py -- Sets important paths for scripts which
# are called via web ajax requests, so to keep it in one place we use it for
# initial setup as well.

load_env = imp.load_source("loadenv", 
                os.path.join(rfid.WEB_FOLDER, 'scripts', 'load_env.py'))
for path in load_env.getpaths():
    sys.path.append(path)

import wsgi_parser as wsgiparser

def application(environ, start_response):

    try:
        output = wsgiparser.parse_wsgi_tags(
            open(rfid.WEB_ENTRY_POINT).read()) # index.html
    except Exception as E:
        tb = traceback.format_exc()
        output="<html><head></head><body>Error: %s<br />%s<br /></body></html>" % (
            str(E), tb)
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    yield output
