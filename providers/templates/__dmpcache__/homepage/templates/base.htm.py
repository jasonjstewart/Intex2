# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554927332.9652994
_enable_loop = True
_template_filename = '/mnt/c/Users/rskal/IS413/Intex/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'header', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n        <title>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n        </title>\n\n')
        __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n        <link id="theme" rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css">\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">\n        \n        <script>\n\n        function lights(sheet, button, showButton) {\n            document.getElementById("theme").setAttribute("href", sheet);\n            button.style.display = \'none\';\n            showButton.style.display = \'block\';\n        }\n\n        function initiate() {\n            var darkMode = document.getElementById("darkModeButton");\n            var lightMode = document.getElementById("lightModeButton");\n\n            darkMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/darkly/bootstrap.min.css", darkMode, lightMode) };\n            lightMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css", lightMode, darkMode) };\n\n            darkMode.style.display = \'block\';\n            lightMode.style.display = \'none\';\n        }\n\n        window.onload = initiate;\n\n\n        </script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n\n        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">\n            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">\n                <span class="navbar-toggler-icon"></span>\n            </button>\n              <a class="navbar-brand" href="/">\n                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/drugs.png" width="50" height="50" alt="">\n                Opioid Tracker\n                </a>\n\n            <div class="collapse navbar-collapse" id="navbarColor01">\n                <ul class="navbar-nav mr-auto">\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else ''))
        __M_writer('">\n                    <a class="nav-link" href="/">Home</a>\n                </li>\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'providers' else ''))
        __M_writer('">\n                    <a class="nav-link" href="/providers">Providers</a>\n                </li>\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'drugs' else ''))
        __M_writer('">\n                    <a class="nav-link" href="/drugs">Drugs</a>\n                </li>\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer('">\n                    <a class="nav-link" href="/about">About</a>\n                </li>\n                </ul>        \n                    <button id="darkModeButton" class="btn btn-secondary" style="margin-left: 10px; display: none;">Lights Off</button>\n                    <button id="lightModeButton" class="btn btn-secondary" style="margin-left: 10px;">Lights On</button>\n                    <a class="btn btn-secondary my-2 my-sm-0" style="margin-left: 10px;" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '/account/logout' if user.is_authenticated else '/account' ))
        __M_writer('" >')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Logout' if user.is_authenticated else 'Login'))
        __M_writer('</a>\n                    <a href="account/signup" class="btn btn-success" role="button" style="margin-left: 10px; display: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'none' if user.is_authenticated else 'block' ))
        __M_writer('">Sign Up</a>\n            </div>\n        </nav>\n\n        <header>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n        </header>\n\n        <main>\n            <div id = content>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            </div>\n        </main>\n\n        <footer>\n            <div class="footer text-primary">\n                <p>Powered by SCRM Consulting</p>\n                <p>Copyright &copy; 2019</p>\n            </div>\n        </footer>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n            Opiate Tracker\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                    Site content goes here in sub-templates.\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/c/Users/rskal/IS413/Intex/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "33": 2, "38": 9, "39": 13, "40": 45, "41": 46, "42": 46, "43": 56, "44": 56, "45": 62, "46": 62, "47": 65, "48": 65, "49": 68, "50": 68, "51": 71, "52": 71, "53": 77, "54": 77, "55": 77, "56": 77, "57": 78, "58": 78, "63": 84, "68": 91, "74": 7, "80": 7, "86": 83, "92": 83, "98": 89, "104": 89, "110": 104}}
__M_END_METADATA
"""
