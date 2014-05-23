'''
:Description:
    wsgi_parser contains methods that read in html files for <? ?> 
    tags and parse their contents in order to return python results 
    into the page.
    
    easy.wsgi then outputs the resulting html code.
    
    Author: Daniel Kettle
    Date: May 22 2014
    
'''

import config, os, re
from lxml import etree as ElementTree
import logging
import datetime

logging.basicConfig(filename='/var/log/easywsgi/parser.log', filemode='w',
                   level=logging.DEBUG)

def custom_parser(statement):
    # use regex to grab an equals sign if NOT in () enclosure
    # If = exists to left of (), assign it a variable
    # Continue parsing right of = or whole statement if not found
    # Look for ()
    # parse arguments and kwargs inside () if applicable
    return eval(statement)

def parse(source):
    '''
    '''
    logging.debug("Beginning parsing source {}".format(source))
    pattern = re.compile('\<\?\s(.*?)\s\?\>')
    matches = pattern.findall(source)
    for m in matches:
        logging.debug("Found tag {}".format(m))
        source = pattern.sub(str(custom_parser(m)), source, count=1) # Only replace this instance of the string
    
    logging.debug("Source after replacement: {}".format(source))
    
    return source

def load_error_page(page, attempted_page, *args, **kwargs):
    '''
    :Description:
        Return error page html without parsing and replacing any tags, as
        we want the error page to be generated and return, unadulterated.
        
    :Returns:
        - string
    '''
    if not os.path.exists(page):
        html = """<html>
<head>
    <title>{}</title>
</head>
<body>
{}
</body>
</html>""".format('Error Page {} not found'.format(page),
                  'Could not find page <b>{}</b> or {} to display error.<br /> Please contact your administrator at {} <br />'.format(attempted_page,
                  page, config.ADMINISTRATOR_EMAIL))
    else:
        html = open(page).read()

    return html

def get_default_html():
    # return xml of empty html xml skeleton
    return """<html><head><title></title></head><body></body></html>"""