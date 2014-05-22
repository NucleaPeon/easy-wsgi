#!/usr/bin/env python3

'''
:Description:
    Python Module that holds configuration options
    
:Options:
    - WEB_FOLDER: list of os.path; Paths to be added to PYTHONPATH, where modules can be located and run.
    - WEB_ENTRY_POINT: os.path; The webpage (usually index.html) that you want wsgi to present to the user
    - JS: os.path; Default javascript contents directory
    - IMAGES: os.path; Default images contents directory
    - CSS: os.path; Default CSS contents directory
    - SCRIPTS: os.path; Default script contents directory
    - LOG_FILE: os.path; Default logfile for state changes
    - ERROR_FILE: os.path; Default logfile for errors
'''

import os, datetime

WEB_FOLDER          = [os.path.join(os.sep, 'var', 'www')]
WEB_ENTRY_POINT     = os.path.join(os.sep, 'var', 'www', 'index.html')

# Set the PYTHONPATH variable to itself plus the WEB_FOLDER
os.environ['PYTHONPATH'] = '{}:{}'.format(
    WEB_FOLDER, os.environ.get('PYTHONPATH', ''))
    
# List web-customizable content folders
JS                  = os.path.join(WEB_FOLDER, 'javascript')
IMAGES              = os.path.join(WEB_FOLDER, 'images')
CSS                 = os.path.join(WEB_FOLDER, 'css')
SCRIPTS             = os.path.join(WEB_FOLDER, 'scripts')
    
# These are fairly sane default log paths. 
LOG_FILE            = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.log')
ERROR_FILE          = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.err')

# Whether to use a Master Template on every loaded page
USE_TEMPLATES = False

# Associate tags with python methods 
MASTER_TEMPLATE = {'*': print}

#
# Example:
#       MASTER_TEMPLATE = {'title': my.module.print_title,
#                          'h1'   : my.biggest.heading}
#