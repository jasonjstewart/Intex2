# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554765577.520532
_enable_loop = True
_template_filename = 'C:/Users/Jaxon/desktop/intex2/Intex2/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'header', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <title>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n        </title>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\r\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\r\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\r\n        <link id="theme" rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/darkly/bootstrap.min.css">\r\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">\r\n        \r\n        <script>\r\n\r\n        function lights(sheet, button, showButton) {\r\n            document.getElementById("theme").setAttribute("href", sheet);\r\n            button.style.display = \'none\';\r\n            showButton.style.display = \'block\';\r\n        }\r\n\r\n        function initiate() {\r\n            var darkMode = document.getElementById("darkModeButton");\r\n            var lightMode = document.getElementById("lightModeButton");\r\n\r\n            darkMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/darkly/bootstrap.min.css", darkMode, lightMode) };\r\n            lightMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css", lightMode, darkMode) };\r\n\r\n            darkMode.style.display = \'none\';\r\n            lightMode.style.display = \'block\';\r\n        }\r\n\r\n        window.onload = initiate;\r\n\r\n\r\n        </script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">\r\n            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">\r\n                <span class="navbar-toggler-icon"></span>\r\n            </button>\r\n\r\n            <div class="collapse navbar-collapse" id="navbarColor01">\r\n                <ul class="navbar-nav mr-auto">\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/">Home</a>\r\n                </li>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'providers' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/providers">Providers</a>\r\n                </li>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'drugs' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/drugs">Drugs</a>\r\n                </li>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/about">About</a>\r\n                </li>\r\n                </ul>        \r\n                    <button id="darkModeButton" class="btn btn-secondary" style="margin-left: 10px; display: none;">Lights Off</button>\r\n                    <button id="lightModeButton" class="btn btn-secondary" style="margin-left: 10px;">Lights On</button>\r\n                    <a class="btn btn-secondary my-2 my-sm-0" style="margin-left: 10px;" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '/account/logout' if user.is_authenticated else '/account' ))
        __M_writer('" >')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Logout' if user.is_authenticated else 'Login'))
        __M_writer('</a>\r\n\r\n            </div>\r\n        </nav>\r\n\r\n        <header>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n            <div><a href="http://django-mako-plus.readthedocs.io/">Online Documentation</a></div>\r\n            <div><a href="https://github.com/doconix/django-mako-plus/">DMP on GitHub</a></div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n            DMP\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" />\r\n                <div class="title">Welcome to <br/> DMP!</div>\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Jaxon/desktop/intex2/Intex2/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "33": 2, "38": 9, "39": 13, "40": 45, "41": 46, "42": 46, "43": 58, "44": 58, "45": 61, "46": 61, "47": 64, "48": 64, "49": 67, "50": 67, "51": 73, "52": 73, "53": 73, "54": 73, "59": 82, "64": 88, "70": 7, "76": 7, "82": 79, "90": 79, "91": 80, "92": 80, "98": 86, "104": 86, "110": 104}}
__M_END_METADATA
"""
