# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554758813.1685038
_enable_loop = True
_template_filename = '/mnt/c/Users/rskal/IS413/Intex/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="card-deck">\n        <div class="card border-info">\n            <div class="card-body"> \n            \n                <i class="fas fa-user-md fa-9x" style="color: #18BC9C"></i>\n                <br />\n                <br />\n                <a href="/providers" class="btn btn-info btn-lg btn-block" role="button">Providers</a>\n\n            </div>\n        </div>\n        <div class="card border-info">\n            <div class="card-body">\n\n                <i class="fas fa-prescription-bottle fa-9x" style="color: #18BC9C"></i>\n                <br />\n                <br />\n                <a href="/drugs" class="btn btn-info btn-lg btn-block" role="button">Drugs</a>\n\n            </div>\n        </div>\n        <div class="card border-info">\n            <div class="card-body">\n            \n                <i class="fas fa-info fa-9x" style="color: #18BC9C"></i>\n                <br />\n                <br />\n                <a href="/about" class="btn btn-info btn-lg btn-block" role="button">About</a>\n                \n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/c/Users/rskal/IS413/Intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 36, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""
