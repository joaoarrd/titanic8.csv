# encoding: utf-8
# module pandas._libs.hashtable
# from C:\Users\marco\PycharmProjects\aulateste\venv\lib\site-packages\pandas\_libs\hashtable.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\marco\PycharmProjects\aulateste\venv\lib\site-packages\numpy\__init__.py

from .HashTable import HashTable

class Int8HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[int8]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                mask : ndarray[bool], optional
                    If not None, the mask is used as indicator for missing values
                    (True = missing, False = valid) instead of `na_value` or
                    condition "val != val".
        
                Returns
                -------
                uniques : ndarray[int8]
                    Unique values of input, not sorted
                labels : ndarray[intp_t]
                    The labels from values to uniques
        """
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        """ returns infos about the state of the hashtable """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[int8]
                    Array of values of which unique will be calculated
                return_inverse : bool, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[int8]
                    Unique values of input, not sorted
                labels : ndarray[intp_t] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[int8]
                    Array of values of which unique will be calculated
                uniques : Int8Vector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                ignore_na : bool, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                mask : ndarray[bool], optional
                    If not None, the mask is used as indicator for missing values
                    (True = missing, False = valid) instead of `na_value` or
                    condition "val != val".
                return_inverse : bool, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[int8]
                    Unique values of input, not sorted
                labels : ndarray[intp_t] (if return_inverse=True)
                    The labels from values to uniques
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A9FE900C30>'


