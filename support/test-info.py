#!/usr/bin/env python

import sys, re, json

class Library(str):
    def __init__(self, value):
        self.name = value

from utils import context
class FakeScenario:
    def __init__(self):
        self.library = Library('ruby')
context.scenario = FakeScenario()

info = {}

mod_name = sys.argv[1]
__import__(mod_name)
mod = sys.modules[mod_name]
info[mod_name] = {}
for cls_name in dir(mod):
    if re.match('Test_', cls_name):
        cls = getattr(mod, cls_name)
        if hasattr(cls, 'pytestmark'):
            for mark in cls.pytestmark:
                if mark.name == 'scenario':
                    info[mod_name][cls_name] = {
                        'scenario': mark.args[0],
                    }

print(json.dumps(info))
