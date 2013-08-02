#import imp, os, re, sys, config

'''
Class that contains two parts:
    - replacement of tags with tags + persistant data as specified in config file
    - regex replacement for <?wsgi ?> method calls in html for dynamic content
'''

def persistant_load():
    """
    :Description:
        Reads and outputs all contents specified by PERSISTANT_LOAD list in
        your config.py file
        
        This is to maintain a constant look and feel regardless of the page 
        that gets loaded by auto-appending contents to specified tags
        
    :Returns:
        - string: html code
    """
    ### TODO
    output = ''
    for htmlfile in config.PERSISTANT_LOAD.keys():
        pass #FIXME this will need to configure each tag.
        
    return output

def parse_html(original, **kwargs):
    """
    :Description:
        WSGI Helper method to load html templates and parse the wsgi
        tags that may be found in them. If this method is not called,
        then only strings will be read and native html markups applied.
        (That means any <?wsgi ?> tags will NOT be visible or utilized
        when a string containing them is passed in *without* calling
        this method.
        
    :Parameters:
        - original: string; html file in its entirety
        - **kwargs: dict; contains pairs of {tag: text} that text gets 
          appended right after the tag found in the html string `original`
        
    :See:
        - config.WEB_FOLDER: Defaults to /var/www/easy-wsgi-conf]
        
    :Returns:
        - string; string `original` with replacements made
    """
    for tag, tagval in kwargs
        original.replace(tag, tagval)
        
    # FIXME: when replacing values, any regular text values will get 
    # replaced to, such as if you are explaining what a <html> tag is.
    return original

def replace_in_html(html_contents, wsgi_string, wsgi_result):
    """
    :Description:
        Replaces the wsgi tag with the wsgi result
    """
    return re.sub(r'''<\?wsgi %s \?>''' % wsgi_string,
                     str(wsgi_result), html_contents)

def call_wsgi_command(cmd_tuple):
    """
    :Description:
        Calls and returns the python command specified by wsgi, does NOT 
        convert it to a string format.
        Arguments for methods are ALWAYS in a string.
        
        DANGER:
            You may need to parse the string if you are expecting a list or tuple or 
            dictionary. You *may* have to use eval, but it is DANGEROUS!
        
    :Parameters:
        - cmd_tuple: tuple or list in format (module, (...), args,) where the 
          (...) refers to a tuple where one or more strings can be specified;
          a minimum of a method call must be specified (without ending ()'s )
          that is lead up by zero-or-more python components (such as classes).
        :example:
            (<module datetime>, ('datetime', 'now',)) -> current datetime
            
    :Returns:
        Result of python method call
        
    #FIXME: Remove debug logs, need pyunit tests, remove python2.x formats if applicable,
            raise error instead of return string, at least gather string from error message.
    """

    mod = None
    # Check for "." in the module path: If found, this is a customized
    # module that we import using full absolute path; otherwise we
    # attempt a simple __import__ on that module, which works for official
    # imports and modules on the sys.path (customs won't be)
    
    a = open("/tmp/test.log", "a")
    if "." in cmd_tuple[0]:
        modname = cmd_tuple[0].split(".")
        modname = modname[len(modname) - 1]
        f, filename, desc = imp.find_module(modname)
        mod = imp.load_module(modname, f, filename, desc)
    else:
        mod         = __import__(cmd_tuple[0])
    if mod == None:
        return "Error: WSGI Module Import invalid; Got 'NoneType'"
    
    # Arguments parsed here:
    funcbuild = mod
    
    for x in cmd_tuple[1]:
        funcbuild = getattr(mod, x)

    if cmd_tuple[2]:
        # TODO: Parse to make arguments sane (strings don't pass properly)
        arguments = cmd_tuple[2].split(" ")
        proper_args = []
        started = False
        quoted_arg = ''
        for arg in arguments:
            if not arg:
                continue
            if arg[0] == '"':
                started = True
                quoted_arg = arg.strip('"')
                if quoted_arg[len(quoted_arg) - 1] == '"':
                    started = False
                    proper_args.append(quoted_arg)
                    continue
            elif arg[len(arg) - 1] == '"':
                quoted_arg += " " + arg.strip('"')
                started = False
                proper_args.append(quoted_arg)
            else:
                if not started:
                    proper_args.append(arg)
                else:
                    quoted_arg += " " + arg
        return funcbuild(*proper_args)
    return funcbuild()
    

def parse_wsgi_tags(html_contents):
    """
    :Description:
        Find all wsgi tags found in the html body and for each instance,
        call a method to determine the python values of the method call,
        then replace the results of the method call with the tag for the
        html body.
        
        Each step is done in a different method. Actual replacement is done
        here.
        
    :Parameters:
        - html_contents: string of the entire html file
        
    :Returns:
        String of html contents with replaced wsgi tags and results.
    """
        
    m = re.findall('<\?wsgi(.*)\?>', html_contents)
    mod     = ''
    classes = ''
    args    = ''
    new_contents = ''
    for pystring in m:
        
        pystring = pystring.strip()
        if pystring:
            parsed = pystring.split(' ') # list [mod, method/class, args]
            mod = parsed[0]
            classes = parsed[1].split('.')
            try:
                # Place arguments in a string, not as a list
                args = ' '.join(parsed[2:])
            except:
                pass
            passin = [mod, classes, args]
            result = call_wsgi_command(passin)
            html_contents = replace_in_html(html_contents, pystring, result)
            
    return html_contents
