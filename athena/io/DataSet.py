#-*- coding:utf-8 -*-


'''
The purpose of this class is to make a generalization of data importing process
so that it's possible for us to keep track of all metadata.

To illustrate part of the benefit, here is an examples:

    If we train a model using a data set, say traffic network flow, and spot
    a few outliers. We may want to know if there are any common features
    among these points? Are they from the same sampling batch? Do they belong to a
    specific connection? Such questions may shed light on the task we are dealing with.

'''

import numpy as np

__author__ = "Xiaoyu Liu"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Prototype"  # one of the three: prototype,development,production

class DataSet(object):

    '''
       the union of all DataPoints.
       The primary usage is to generate and populate the needed data.

       input: data file
       output: a DataSet item.
    '''










