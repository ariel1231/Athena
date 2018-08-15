#-*- coding:utf-8 -*-

import numpy as np

__author__ = "Xiaoyu Liu"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Prototype"  # one of the three: prototype,development,production

class Attribute(object):
   """
   to be filled
   """
   def __init__(self,attribute_name,is_numerical=None,description=None):
        self.name = attribute_name
        self.is_numerical = is_numerical
        self.description = description
        self.map = None # This is a mapper from string value to integer value
        self.numerical_label = None # value to name

   #TODO: add a neat __str__



