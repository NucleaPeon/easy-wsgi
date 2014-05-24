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
    # Regex Description:
    # 
    # Expects 0 or 1 "=" signs in the string before the brackets ()
    # The string(s) returned are:
    #   If before the = sign (if applicable): no periods allowed
    #   If after the = sign, periods are allowed, up until the (
    #   Anything between the ( and ) is put into another group.
    #
    # Ends after the () 

    pattern = re.compile('([\w^\.]*)=?([\w\.]+)*(\((.*)\)|\Z)') 
    def parse_attributes(*args):
        # arg[0] is either variablename or import-to-method (asdf from `asdf=datetime.datetime.now`
        #       or datetime.datetime.now if variable name not assigned)
        # arg[1] module and method path name reference (ex: datetime.datetime.now)
        #       This only applies if a variablename is used. if arg[1] not None, arg[0] = arg[1]
        # arg[2] is what is between the brackets (or empty if no brackets in case of just module/method ref)
        #       If there is something in between the brackets, arg[3] is not None. Else this will be empty or "()"
        # arg[3] If args/kwargs are used, this is the string.
        
        # In order to parse kwargs, use this regular expression: 
        # (\w*)|\w*=*\w*|\"(.*?)" # NOT DONE, almost done
        # (test code)
        # "hello world", 5, kwarg="something, something, something else" 
        #result = eval(args[0] + args[2])
        #logging.debug("result is {}".format(args[0] + args[2]))
        #return args[0] + args[2]
        return args[0][0] + args[0][2]
    
    return eval(parse_attributes(pattern.search(statement).groups()))

def parse(source):
    '''
    '''
    pattern = re.compile('\<\?\s(.*?)\s\?\>') # <? ?> tags
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