#!/usr/bin/env python

# Global Python imports and then add the configuration file import for 
# directory paths.
import os, sys, traceback, logging
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import config, wsgi_parser

logging.basicConfig(filename='/var/log/easywsgi/example.log', filemode='a',
                   level=logging.DEBUG)

def application(environ, start_response):

    logging.debug(str(environ))
    try:
        if config.USE_TEMPLATES:
            # Read in Html File:
            logging.debug("Using Templates, found keys: {}".format(config.MASTER_TEMPLATE.keys()))
            path = environ.get('REQUEST_URI')
            if not os.path.exists(path) or path == config.ERRORS.get('404'):
                # Failed to obtain a valid path, or we *want* to visit the error page
                logging.error("Requested path to {}, ended in {}".format(environ.get('REQUEST_URI'),
                                                                         path))
                output = wsgi_parser.load_error_page(config.ERRORS.get('404'),
                                                  environ.get('REQUEST_URI'))
            else:                                  
                output = ['''<b>Hello World</b>''']
                output.append('''This is a new line in code, but only a <br /> does a new line in html''')
        
    except Exception as E:
        tb = traceback.format_exc()
        logging.error(str(E) + ", " + tb)
        
    # Break down organized html code into one byte string:
    output = bytes('\n'.join(output), encoding="UTF-8")
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    yield output 