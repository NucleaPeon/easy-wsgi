easy-wsgi
========

WSGI mini-framework that is easy to set up and configure to serve
dynamic content in html pages.

TODO
========

* wsgi_parser needs work before it can render webpages properly.
* Documentation and Installation docs need to be written
* easy-wsgi.py needs work
* Safe eval() capabilities for arguments
* Tags read by regex

Examples
========

Templating
------

Tag Format:

`<? [(optional)variablename]=path.to.module.class_or_method(args, kwargs) ?>`

The format is similar to a basic python statement. easy-wsgi allows a user to
assign the results of a method or class into a variable name. 

    * `name=statement`: there can be no spaces between your variable name, equals sign and the statement
    
The path to the module is separated by periods ".", although to use python build-ins,
you won't be using any modules.

    * <? print("hello world") ?> <!-- no modules -->
    * <? my.module.method.print("hello world") ?> <!-- my module -->
    * <? length=len([1, 4, 5, 6, 7]) ?>

At the end of the module path (if applicable, otherwise the statement), you can
have a class or a method, or both.

    * class: <? obj=my.module.method.MyClass() ?>
      <? obj.method() ?>
    * method: <? m=my.module.do_something() ?>
    * both: <? m=my.module.method.MyClass().method() ?> <!-- this works best in singleton patterns or one-offs -->
    * also: <? m=my.module.do_something ?> <!-- stores method in "m" variable -->
    
In a future release it may be possible to have complex arguments in methods 
and classes (dict, list), but for now we limit it to int/float/string/bool.

Master Template Example
------

If you want every single `<title>` tag to be generated that goes through easy-wsgi,
use a **Master Template**. 

This is done by:

    * Enabling `USE_TEMPLATES = True` in config.py
    * Associating the 'title' key in the MASTER_TEMPLATE dictionary to a method
    * Writing a <title></title> tag into your page

Each title tag should return the results of the method inside.
(for tag modifiers themselves, please use javascript)


