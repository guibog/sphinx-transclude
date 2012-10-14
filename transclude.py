# -*- encoding: utf8 -*-

"""A transclusion directive for sphinx documenter"""

# guibog@gmail.com
#
# https://github.com/guibog/sphinx-transclude

import pprint
import os
import pickle
from docutils import nodes
from sphinx.util.compat import Directive

isa = isinstance

class TranscludeDirective(Directive):
    required_arguments = 2
    def run(self):
        source, target = self.arguments
        return [transclude(source=source, target=target)]

class transclude(nodes.General, nodes.Element):
    pass

class WrongSourceDoctree():
    ids = []
    def __init__(self, err):
        self.err = err

def setup(app):
    app.add_node(transclude)
    app.add_directive('transclude', TranscludeDirective)
    app.connect('doctree-resolved', process_transclusions)

def _load_source_doctree(env, source):
    path = os.path.join(env.doctreedir, "%s.doctree" % source)
    try:
        f = open(path)
        return pickle.load(f)
    except IOError, err:
        return WrongSourceDoctree(err)

def process_transclusions(app, doctree, fromdocname):
    env = app.builder.env
    #pprint.pprint(env.__dict__)
    doctrees = {}
    for node in doctree.traverse(transclude):
        source = node.attributes['source']
        target = node.attributes['target']
        if source not in doctrees:
            doctrees[source] = _load_source_doctree(env, source)
        if isa(doctrees[source], WrongSourceDoctree):
            err = "Unable to find source %s" % source
            node.replace_self(nodes.problematic(err, err))
        elif target in doctrees[source].ids:
            node.replace_self(doctrees[source].ids[target])
        else:
            err = "Unable to find target %s in source %s" % (target, source)
            node.replace_self(nodes.problematic(err, err))
