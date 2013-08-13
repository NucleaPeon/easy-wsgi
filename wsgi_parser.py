import imp, os, re, sys, config, importlib

'''
Class that contains two parts:
    - replacement of tags with tags + persistant data as specified in config file
    - regex replacement for <?wsgi ?> method calls in html for dynamic content
'''

class Html():
    '''
    TODO: 
        - [x] Generate basic html file when no html file specified.
        - [x] Generate input html file when specified
        - Replace tag in both basic generated html and specified html
            - wsgi tag
            - wsgi-template tag
        - python method calling and return results as string
    '''
    htmlfile = ''
    structure = {}
    
    def __init__(self, **kwargs):
        '''
        :Description:
            Initializes the html code in an object for parsing. One html page per
            object.

        :Parameters:
            - **kwargs: dict; keyword arguments
            - htmlfile: string; path to html file
            - htmlcontents: string; html code to manipulate directly
        '''
        if kwargs.get('htmlfile', ''):
            self.htmlfile = open(kwargs['htmlfile']).read()
        if kwargs.get('htmlcontents', ''):
            self.htmlfile = kwargs['htmlcontents']
        if not self.htmlfile:
                # FIXME: Templates
            self.structure['html']  = '<html>' #config.TEMPLATES.get("html", '<html>')
            self.structure['/html'] = '</html>' #config.TEMPLATES.get("/html", '</html>')
            self.structure['head']  = '<head>' #config.TEMPLATES.get("head", '<head>')
            self.structure['/head'] = '</head>' #config.TEMPLATES.get("/head", '</head>')
            self.structure['body']  = '<body>' #config.TEMPLATES.get("body", '<body>')
            self.structure['/body'] = '</body>' #config.TEMPLATES.get("/body", '</body>')
            
            self.htmlfile = '''{}\n{}\n{}\n{}\n{}\n{}\n'''.format(
                self.structure['html'], self.structure['head'], self.structure['/head'],
                self.structure['body'], self.structure['/body'], self.structure['/html'])
                
            
    def __str__(self):
        return '{}'.format(self.htmlfile)
    
    def parse(self):
        '''
        :Description:
            Replaces html contents tags with the results of the method call
            specified in the tag. If Templates are enabled, it also searches
            for template tags.
            
            
            Templates are not recommended on pages where the main tags:
                - html
                - body
                - head
            are manipulated because we can either replace ALL instances of
            <tag> with the Template, or the first instance. Even if comments
            are stripped out that may contain the strings, jQuery may require
            <tag> references (or at least javascript), so this method is
            dangerous. The *correct* solution to using templates is to not
            use any input files whatsoever. In fact, if parse() detects
            a None input file, it will auto generate to the best of its ability,
            a functioning html file even if it ends up blank.
            
            Because Templates are created first, then wsgi tags are parsed,
            a template can reference a python method so absolutely NO
            html file is required for wsgi to run properly.
            Cool trick eh?
            
        :Parameters:
            - htmlcontents: string; html code to configure with Template
              
        :Returns:
            - string; output of replaced input file with corrections made
        '''
        self.html = htmlcontents
        return htmlcontents
        templatedhtml = []
        # Must append in order
        if not htmlcontents is None:
            # we have a string to replace
            templatedhtml = open(htmlcontents, 'r').read()
            for key in self.structure.keys():
                if not self.structure.get(key) is None:
                    templatedhtml.replace(key, 
                                          self.structure[key])
                
        else:
            for x in ['html', 'head', '/head', 'body', '/body', '/html']:
                if self.structure.get(x) is None:
                    templatedhtml.append('<{}>'.format(x))
                else:
                    templatedhtml.append(self.structure[x])
        return templatedhtml

    #def __replace_tag(html_contents, wsgi_string, wsgi_result):
        #"""
        #:Description:
            #Replaces the wsgi tag with the wsgi result.
            #This method does not actually *call* the wsgi method, nor
            #ensure that the module and class and arguments are parsed.
            #It's a simple "go through html file and replace tags with
            #result".
        
        #:Parameters:
            #- html_contents: string; entire html file
            #- wsgi_string: the tag complete with module, class and args
            #- wsgi_result: the returned value(s) of the method call
        #"""
        #return re.sub(r'''{}'''.format(wsgi_string),
                     #str(wsgi_result), html_contents)

    """
    def __call_wsgi(*cmd_tuple):
        '''
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
            Please note that wsgi is meant for calling module-level methods,
            not class methods, although it should be possible by specifying
            using period delimited module paths in <wsgi ?> tags.
                
        :Returns:
            Result of python method call
        '''
        # Check for "." in the module path: If found, this is a customized
        # module that we import using full absolute path; otherwise we
        # attempt a simple __import__ on that module, which works for official
        # imports and modules on the sys.path (customs won't be)
        
        cmd_tuple = tuple([x for x in cmd_tuple if bool(x)])
    #    if mod == None:
    #        raise Exception("Error: WSGI Module Import invalid; Got 'NoneType'")
        modpath = cmd_tuple[0].split('.')
        if len(modpath) > 1:
            # Parse period-separated string into list, module import name should be
            # in last position, import path is rest of array
            tuple_sep = len(modpath) - 1
            mod = importlib.import_module(modpath[tuple_sep], modpath[:tuple_sep])
        else:
            mod     = importlib.import_module(modpath[0])
        classes = cmd_tuple[1]
        method  = cmd_tuple[2]
        try:
            args = cmd_tuple[3:]
        except:
            pass
        # Arguments parsed here:
        funcbuild = getattr(mod, cmd_tuple[1])
        funcbuild = getattr(funcbuild, cmd_tuple[2])
        retval = funcbuild
        if len(cmd_tuple) > 3: # (mod, method, func)
            return funcbuild(*cmd_tuple[:3])
        return retval()
    """