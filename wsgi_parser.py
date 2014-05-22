'''
:Description:
    wsgi_parser contains methods that read in html files for <? ?> 
    tags and parse their contents in order to return python results 
    into the page.
    
    easy.wsgi then outputs the resulting html code.
    
    Author: Daniel Kettle
    Date: May 22 2014
    
'''

import config, os

def template_tag(tag, method, *args, **kwargs):
    '''
    :Description:
        Read the config.py module and replace tag bodies with contents
    '''
    pass

def load_error_page(page, attempted_page, *args, **kwargs):
    '''
    :Description:
        Return error page html without parsing and replacing any tags, as
        we want the error page to be generated and return, unadulterated.
        
    :Returns:
        - string
    '''
    if not os.path.exists(page):
        html = ["""<html>
<head>
    <title>{}</title>
</head>
<body>
{}
</body>
</html>""".format('Page {} not found'.format(page),
                  'Could not find page {}.<br /> Please contact your administrator at {} <br />'.format(attempted_page,
                  config.ADMINISTRATOR_EMAIL))]
    else:
        html = [open(page).read()]
    return html
