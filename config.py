#!/usr/bin/env python

'''
:Description:
    Configuration file (as a python module) that determines the
    behaviour of easy-wsgi. 
    
:Options:
    - WEB_FOLDER: string path; Similar to the Directory tag of apache2, this points to the folder where wsgi contents are contained. This will be added to the PYTHONPATH variable.
    - WEB_ENTRY_POINT: string path; The webpage (usually index.html) that you want wsgi to present to the user when they enter in the root (usually the hostname (localhost or domain name))
    - JS: string path; Default javascript contents directory
    - IMAGES: string path; Default images contents directory
    - CSS: string path; Default CSS contents directory
    - SCRIPTS: string path; Default script contents directory
    - LOG_FILE: string path; Default logfile for state changes
    - ERROR_FILE: string path; Default logfile for errors
'''
import os, datetime
WEB_FOLDER          = os.path.join(os.sep, 'var', 'www', 'default')
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

# Whether to parse <?wsgi-template ?> tags, pointing to a python file with required methods
# Example:
#   <?wsgi-template title import.python.module *args ?>
# would replace the <title> tag with import.python.module.title
# - method is the name of the tag. *args can contain 'end_bracket' string
#   which forces the </tag> instead of <tag>

USE_TEMPLATES = False

# Format is {tag : path to load for tag -or- a literal string}
# Explaination:
#   Persistant load is a way in which a tag will always have contents
#   appended to it regardless of which page is produced
#   For example, always having a sidebar for navigation in the <body> tag.
#
#   If you want an entire file read, use: open(os.path.join(
#       path, to, file)).read() 
#   in the place of the string. It is a good idea to modularize your code
#   and place small snippets or files here.
#TEMPLATES     = {'html': '<!--\n Author: \nDate: {}\n-->'.format(str(datetime.datetime.now())),
#                 '/html': '</html>'}
