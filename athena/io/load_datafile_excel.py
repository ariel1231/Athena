#-*- coding:utf-8 -*-

import numpy as np
import io
import re
import csv




__author__ = "Xiaoyu Liu"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Prototype"  # one of the three: prototype,development,production


def load_entire_datafile(filename):

    # create an empty container
    fileContent = list()

    # r means read, b means data object
    with open(filename,'r') as datFile:
        freader = csv.reader(datFile,delimiter=',')
        for row in freader:
            fileContent.append(row)

    return fileContent

def _parse_fileContent(fileContent):

    # TODO : fill the documentation
    '''
    in this very simple version, the first line is the header
    others are the data contents while the last column is data labels.

    Returns
    1. a tuple of an array of attribute names and an array of attribute
    values.
    2.
    '''
    attrnames = tuple(fileContent[0])
    dat = np.array(fileContent[1:])


    return (attrnames,dat)




def create_data_structure(inputFileName, outputFileName =''):
    '''
    need to be filled
    :return:
    '''
    # TODO: fill the documentation
    data_file = load_entire_datafile(inputFileName)
    attrnames,dat,label_set,numerical_label =_parse_fileContent(data_file)

    # TODO: add a function to save the precessed data to the disk.
    if outputFileName:
        pass
    pass















if __name__ == "__main__":
    filename = "/Users/ariel/Documents/work/Athena/data/iris/iris_data.csv"
    iris_dat = load_entire_datafile(filename)
    print(len(iris_dat))
    attr_name,data = _parse_fileContent(iris_dat)
    print(attr_name,'\t',np.shape(data),'\t first line:',data[0])










