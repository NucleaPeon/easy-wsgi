#!/usr/bin/env python

'''
:Description:
    Configuration file (as a python module) that determines the
    behaviour of easy-wsgi. 
    
:Options:
    - WEB_FOLDER: string path; Similar to the Directory tag of apache2, this points to the folder where wsgi contents are contained. This will be added to the PYTHONPATH variable.
    - WEB_ENTRY_POINT: string path; The webpage (usually index.html) that you want wsgi to present to the user when they enter in the root (usually the hostname (localhost or domain name))
    - 
'''
import os
WEB_FOLDER          = os.path.join(os.sep, 'var', 'www', 'easy-wsgi')
WEB_ENTRY_POINT     = os.path.join(WEB_FOLDER, '..', 'index.html')

# Set the PYTHONPATH variable to itself plus the WEB_FOLDER
os.environ.set('PYTHONPATH', '{}:{}'.format(
    WEB_FOLDER, os.environ.get('PYTHONPATH', ''))
    
# List web-customizable content folders
JS                  = os.path.join(WEB_FOLDER, 'javascript')
IMAGES              = os.path.join(WEB_FOLDER, 'images')
CSS                 = os.path.join(WEB_FOLDER, 'css')
SCRIPTS             = os.path.join(WEB_FOLDER, 'scripts')
    
# These are fairly sane default log paths. 
LOG_FILE            = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.log')
ERROR_FILE          = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.err')

