# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554755429.3792737
_enable_loop = True
_template_filename = 'C:/Users/Jaxon/desktop/intex2/Intex2/account/templates/logout.html'
_template_uri = 'logout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['header', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="form-box">\r\n        <div class="head">Login to<br>Prescription Tracker</div>\r\n        <form id="login-form" method="POST">\r\n            <p>You have been successfully logged out!</p>\r\n            <a id="login_redirect" href="/account/index" class="btn btn-primary">Login</a>\r\n        </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Jaxon/desktop/intex2/Intex2/account/templates/logout.html", "uri": "logout.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 11, "48": 15, "54": 3, "60": 3, "66": 13, "72": 13, "78": 72}}
__M_END_METADATA
"""
