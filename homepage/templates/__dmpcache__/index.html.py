# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554949787.6701195
_enable_loop = True
_template_filename = '/mnt/c/Users/rskal/IS413/Intex/homepage/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/drugs.png" alt="drugs" style="height: 210px;" />\n    <div class="title text-primary" style="font-size: 50px;">Welcome to <br /> Opioid Prescription Tracker</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="card-deck">\n        <div class="card bg-primary" style="border-width: 0px; border-radius: 20px">\n            <div class="card-body"> \n            \n                <i class="fas fa-search fa-9x text-danger"></i>\n                <br />\n                <br />\n                <a href="/search/" class="btn btn-secondary btn-lg btn-block" role="button">Search</a>\n\n            </div>\n        </div>\n        <div class="card bg-primary" style="border-width: 0px; border-radius: 20px">\n            <div class="card-body">\n\n                <i class="fas fa-chart-area fa-9x text-danger"></i>\n                <br />\n                <br />\n                <a href="/analytics" class="btn btn-secondary btn-lg btn-block" role="button">Analytics</a>\n\n            </div>\n        </div>\n        <div class="card bg-primary" style="border-width: 0px; border-radius: 20px">\n            <div class="card-body">\n            \n                <i class="fas fa-info fa-9x text-danger"></i>\n                <br />\n                <br />\n                <a href="/about" class="btn btn-secondary btn-lg btn-block" role="button">About</a>\n                \n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/c/Users/rskal/IS413/Intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 7, "50": 42, "56": 3, "64": 3, "65": 5, "66": 5, "72": 9, "78": 9, "84": 78}}
__M_END_METADATA
"""
