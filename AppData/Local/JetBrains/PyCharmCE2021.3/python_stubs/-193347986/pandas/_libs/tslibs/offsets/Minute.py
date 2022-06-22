# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\marco\PycharmProjects\novoprojeto\venv\lib\site-packages\pandas\_libs\tslibs\offsets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Program Files\Python310\lib\operator.py
import re as re # C:\Program Files\Python310\lib\re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Program Files\Python310\lib\warnings.py
import numpy as np # C:\Users\marco\PycharmProjects\novoprojeto\venv\lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .Tick import Tick

class Minute(Tick):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _nanos_inc = 60000000000
    _period_dtype_code = 8000
    _prefix = 'T'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FFEC445EC0>'


