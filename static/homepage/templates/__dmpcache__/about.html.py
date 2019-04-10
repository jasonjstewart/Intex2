# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554864014.8126674
_enable_loop = True
_template_filename = 'C:/Users/steve/Desktop/intex2/homepage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="jumbotron" style="max-width: 50%; margin-left: 25%; margin-right: 25%">\r\n        <h1> About Prescription Tracker</h1>\r\n        <br />\r\n        <p>The opioid crisis is devastating communities across America. The latest statistics indicate that the total yearly overdose deaths due to opioids reached a new high of 70,237 in 2017. In that same year, President Trump declared the opioid crisis a public health emergency. </p>\r\n            <br />\r\n        <p>While different measures have been taken to combat the crisis,no web-accessible database is available to allow government officials, healthcare providers, and prescribers to view and analyze the volume of drugs being prescribed... Until Now</p>\r\n            <br />\r\n        <p>OpioidTracker.co was built to help combat the opioid epidemic across america by providing government officials, healthcare providers, and prescribers to view and analyze the volume of drugs being prescribed.</p>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/steve/Desktop/intex2/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 15, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""
