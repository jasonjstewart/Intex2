# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555001782.632679
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
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <title>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n        </title>\r\n\r\n        <link rel="shortcut icon" type="image/png" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/drugs.png"/>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\r\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\r\n        <link id="theme" rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/darkly/bootstrap.min.css">\r\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">\r\n        \r\n        <script>\r\n\r\n        function lights(sheet, button, showButton) {\r\n            document.getElementById("theme").setAttribute("href", sheet);\r\n            button.style.display = \'none\';\r\n            showButton.style.display = \'block\';\r\n        }\r\n\r\n        function initiate() {\r\n            var darkMode = document.getElementById("darkModeButton");\r\n            var lightMode = document.getElementById("lightModeButton");\r\n\r\n            darkMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/darkly/bootstrap.min.css", darkMode, lightMode) };\r\n            lightMode.onclick = function () { lights("https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/flatly/bootstrap.min.css", lightMode, darkMode) };\r\n\r\n            darkMode.style.display = \'none\';\r\n            lightMode.style.display = \'block\';\r\n        }\r\n        \r\n        function showAlert(){\r\n            console.log("run function");\r\n            console.log(document.getElementById("searchAlert"));\r\n            document.getElementById("searchAlert").style.display = \'block\';\r\n        }\r\n\r\n        window.onload = initiate;\r\n\r\n        </script>\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-primary">\r\n            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">\r\n                <span class="navbar-toggler-icon"></span>\r\n            </button>\r\n              <a class="navbar-brand" href="/">\r\n                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/drugs.png" width="50" height="50" alt="">\r\n                Opioid Tracker\r\n                </a>\r\n\r\n            <div class="collapse navbar-collapse" id="navbarColor01">\r\n                <ul class="navbar-nav mr-auto">\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/">Home</a>\r\n                </li>\r\n                <li class="nav-item dropdown ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'prescribers' else ''))
        __M_writer('">\r\n                    <a class="nav-link dropdown-toggle" href="/search" id="searchDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Search</a>\r\n                    <div class="dropdown-menu" aria-labelledby="searchDropdown">\r\n                        <a class="dropdown-item" href="/search/prescribers">Prescriber</a>\r\n                        <a class="dropdown-item" href="/search/drugs">Drugs</a>\r\n                        <a class="dropdown-item" href="/search/prescribersAndDrugs">Prescribers & Drugs</a>\r\n                    </div>\r\n                </li>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.app == 'drugs' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/analytics">Analytics</a>\r\n                </li>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/about">About</a>\r\n                </li>\r\n                </ul>        \r\n                    <p class="userWelcome">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)("Welcome, " + user.username + "!" if user.is_authenticated else ""))
        __M_writer('</p>\r\n                    <button id="darkModeButton" class="btn btn-secondary" style="margin-left: 10px; display: none;">Lights Off</button>\r\n                    <button id="lightModeButton" class="btn btn-secondary" style="margin-left: 10px;">Lights On</button>\r\n                    <a class="btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'btn-danger' if user.is_authenticated else 'btn-success'))
        __M_writer(' my-2 my-sm-0" style="margin-left: 10px;" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '/account/logout' if user.is_authenticated else '/account' ))
        __M_writer('" >')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Logout' if user.is_authenticated else 'Login'))
        __M_writer('</a>\r\n                    <a href="/account/signup" class="btn btn-info" role="button" style="margin-left: 10px; display: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'none' if user.is_authenticated else 'block' ))
        __M_writer('">Sign Up</a>\r\n                    <a class="btn btn-info my-2 my-sm-0" style="margin-left: 10px; display: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'block' if user.is_authenticated and (user.user_type == 4 or user.user_type == 1) else 'none' ))
        __M_writer('" href="/admin">Admin Tools</a>\r\n            </div>\r\n        </nav>\r\n\r\n        <header>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n        </header>\r\n\r\n        <main>\r\n            <div id = content>\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n        <footer>\r\n            <div class="footer text-primary">\r\n                <p>Powered by SCRM Consulting</p>\r\n                <p>Copyright &copy; 2019</p>\r\n            </div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Opiate Tracker\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Jaxon/desktop/intex2/Intex2/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "33": 2, "38": 9, "39": 12, "40": 12, "41": 15, "42": 51, "43": 52, "44": 52, "45": 62, "46": 62, "47": 68, "48": 68, "49": 71, "50": 71, "51": 79, "52": 79, "53": 82, "54": 82, "55": 86, "56": 86, "57": 89, "58": 89, "59": 89, "60": 89, "61": 89, "62": 89, "63": 90, "64": 90, "65": 91, "66": 91, "71": 97, "76": 103, "82": 7, "88": 7, "94": 96, "100": 96, "106": 102, "112": 102, "118": 112}}
__M_END_METADATA
"""
