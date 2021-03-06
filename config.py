#!/usr/bin/env python3

'''
:Description:
    Python Module that holds configuration options
    
:Options:
    - WEB_FOLDER: list of os.path; Paths to be added to PYTHONPATH, where modules can be located and run.
    - WEB_ENTRY_POINT: os.path; The webpage (usually index.html) that you want wsgi to present to the user
      when you access the wsgi application without additional url parameters
    - JS: os.path; Default javascript contents directory
    - IMAGES: os.path; Default images contents directory
    - CSS: os.path; Default CSS contents directory
    - SCRIPTS: os.path; Default script contents directory
    - LOG_FILE: os.path; Default logfile for state changes
    - ERROR_FILE: os.path; Default logfile for errors
'''

import os, sys, datetime

WEB_FOLDER          = os.path.join(os.sep, 'var', 'www')
# Use if you want to redirect user from WEB_FOLDER to a webpage if root is visited
#       Example: http://mysite --> http://mysite/index.html
WEB_ENTRY_POINT     = os.path.join(os.sep, 'var', 'www', 'index.html')
# Use if your code is not in the WEB_FOLDER, this gets added to path
CODE_ENTRY_POINT    = os.path.join(os.sep, 'var', 'www', 'Web')

sys.path.append(WEB_FOLDER)
    
# List web-customizable content folders
JS                  = os.path.join(WEB_FOLDER, 'js')
#IMAGES              = os.path.join(WEB_FOLDER, 'images')
#CSS                 = os.path.join(WEB_FOLDER, 'css')
#SCRIPTS             = os.path.join(WEB_FOLDER, 'scripts')
    
# Paths to Error Pages:
ERRORS = {'404': os.path.join(WEB_FOLDER, 'error404.html')}
    
# These are fairly sane default log paths. 
LOG_FILE            = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.log')
ERROR_FILE          = os.path.join(os.sep, 'var', 'log', 'easy-wsgi.err')

# Whether to use a Master Template on every loaded page
USE_TEMPLATES = True

# Associate tags with python methods 
#       * : Do this for all tags
#       - : Do this for the top of the html page (DOCTYPES, etc)
#       
MASTER_TEMPLATE = {'title': lambda: "Best page in the world"}

#
# Example:
#       MASTER_TEMPLATE = {'title': my.module.print_title,
#                          'h1'   : my.biggest.heading}
#
ADMINISTRATOR_EMAIL = 'admin@example.com'