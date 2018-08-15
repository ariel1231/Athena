#-*- coding:utf-8 -*-


"""
The purpose of this class is to make a generalization of data importing process
so that it's possible for us to keep track of all metadata.

To illustrate part of the benefit, here is an examples:

    If we train a model using a data set, say traffic network flow, and spot
    a few outliers. We may want to know if there are any common features
    among these points? Are they from the same sampling batch? Do they belong to a
    specific connection? Such questions may shed light on the task we are dealing with.

"""

import numpy as np
import copy as cp
from numpy import random as rand
from athena.io import Attribute
from athena.io import DataPoint




__author__ = "Xiaoyu Liu"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Prototype"  # one of the three: prototype,development,production

class DataSet(object):

    """
       the union of all DataPoints.
       The primary usage is to generate and populate the needed data.

       input: data file
       output: a DataSet item.
    """

    # TODO: finish the documentation

    def __init__(self,raw_dat,attr_list=None):
        self.dataIDs = list()
        self.attributes = dict()
        self.dataMatrix = list()

        self._raw_dat = raw_dat
        self._raw_attribute = attr_list




    def generate_id(self,prefix="",length=5):
        """
        generate an unique id for each data point in the data file.
        :param:
        :return:

        # things need to be considered: 1. an efficient way/structure for searching

        """
        #TODO: documentation

        MAX_REPEATED_TIME = 30  # hard coded value
        counter = 0

        id_num = int(rand.random() * 10**length)
        id_num_fixed_length = str(id_num).zfill(length)
        id = prefix + str(id_num_fixed_length)
        while id in self.dataIDs:
            # repeated id identified, generate a new one
            if counter < MAX_REPEATED_TIME:
                id_num = int(rand.random() * 10 ** length) #generate another value
                id_num_fixed_length = str(id_num).zfill(length)
                id = prefix + str(id_num_fixed_length)
                counter = counter + 1
            else:
                raise ValueError("Cannot generate an unique id for the data point! ")

        self.dataIDs.append(id)
        return id

    def add_attributes(self):
        """
        to be done
        :param:
        :return:
        """


        data_array = cp.deepcopy(self._raw_dat)
        sample = data_array[0]

        #TODO: consider situation with 'NA' or empty value
        for i,attrname in enumerate(self._raw_attribute):
            attr = Attribute(attrname)
            if self._is_number(sample[i]):
                attr.is_numerical = True
                #print(attrname,'is numerical')
            else:
                #print(attrname,'is NOT numerical.')
                attr.is_numerical = False
                attr.map = self._generate_mapper(data_array,i)
                attr.numerical_label = {v: k for k, v in attr.map.items()}
            self.attributes[attrname] = attr
        #print(data_array)
        return data_array



    def _generate_mapper(self,data_array,attr_position):
         # change value in data_array so that no string value exists
        mapper = dict()
        label_set = list()
        start_value = 1
        for i,row in enumerate(data_array):
            #print(i,row,attr_position)
            label = row[attr_position]
            if label not in label_set:
                label_set.append(label)
                mapper[label] = start_value
                #print(label,':',start_value)
                data_array[i][attr_position] = start_value
                start_value = start_value + 1
            else:
                data_array[i][attr_position] = mapper[label]
        #print(data_array)
        return mapper





    def setup_data(self,data_point_array):

        """
        MUST CALLED AFTER self.add_attribute.

        :param: data_point_array  a 2d numpy array subject by sample
                                  each row represents a data point while
                                  each column represents an attribute

        :param: attr_list original attribute list

        Here we want to add data points to form a data matrix
        for the dataSet item.
        Notice this is an initial setup function, so attr_list should be
        identical to self.attributes

        """

        if len(self._raw_attribute) is not len(self.attributes):
            raise ValueError("Please try add_data_point_function!")

        for i,item in enumerate(data_point_array):
            unique_id = self.generate_id('iris_')
            data_point = DataPoint(item, unique_id, self._raw_attribute)
            #print(data_point, type(data_point), isinstance(data_point,np.ndarray))
            self.dataMatrix.append(data_point)

        #
        print(self.dataMatrix)
        print(self.dataIDs)










    def _generate_labels(self,label_attr):
        """
        Generate certain labels according to attribute selected.
        Take iris flower data set as an example,
        if classification is based on the category of the flower,
        then the "class" information is used as a label and will iterate over all the
        data points and return the label list.

        :return:
        """
        #TODO : change to the list ops data matrix
        if isinstance(label_attr,list):
            # axis 0 for row , 1 for col
            #print('\n\n',"----"*10, 'debugging label generation','----'*10,'\n\n')
            label_index = self._locate_attr_pos(label_attr)
            label_cols = self.dataMatrix[:,label_index]
            #print(label_cols)
            #TODO: case insensitive case
            #TODO: ordering
            attr_objs = [self.attributes[item] for item in label_attr]
            #print('get attributes',attr_objs)
            #print('How many attributes?', len(attr_objs))
            label_dict = dict()
            legend = dict()
            start = 1
            labels = np.zeros(shape=(len(label_cols),)) #TODO: ensure dataMatrix has multiple points
            #label_dict[str(label_cols[0])] = 1 # ndarray is unhashable, convert to str

            #TODO: Consider redefining __equal__

            for i,item in enumerate(label_cols):
                #print('Here',label_dict,item)
                if str(item) not in label_dict.keys():
                    labels[i] = start
                    label_dict[str(item)] = start
                    labels[i] = label_dict[str(item)]
                    legend_str = list()
                    for j, item in enumerate(attr_objs):
                        #print(item.numerical_label is None, j)
                        if item.numerical_label is None:
                            legend_str.append(str(label_cols[i][j]))
                        else:
                            legend_str.append(item.numerical_label[label_cols[i][j]])
                    legend[start] = '_'.join(legend_str)
                    start = start + 1
                else:
                    labels[i] = label_dict[str(item)]
                #
            #print('legend: ',legend,'\n label:',labels,'\n',"label_dict: ",label_dict)

            return (labels,legend,label_dict)

        elif isinstance(label_attr,dict):
            return


    def generate_data_partition_by_value(self):
        pass

    def generate_data_partition(self,label_attr,attr_list=None):
        """

        generate data matrix for classification tasks.

        :param args: a list of attributes that you want,default, all except for labels
        :return: matrix consists of data points.
        """

        #TODO: Consider ordering for efficiency
        #TODO: figure out the nested ops of list and nparray
        dat = cp.deepcopy(self.dataMatrix)
        #print(type(dat))
        print('original data matrix is of shape',np.shape(dat))
        #print(type(dat[0]))
        if attr_list is not None:
            attr_list_index = self._locate_attr_pos(attr_list)
            # axis 0 for row, 1 for col
            #TODO write a deletion function.
            dat = [np.delete(item,attr_list_index,axis=1) for item in dat]
                #np.delete(dat,attr_list_index,axis=1)
        label_index = self._locate_attr_pos(label_attr)
        #labels,legend,label_dict = self._generate_labels(label_attr)
        # axis 0 for row, 1 for col
        #dat = np.delete(dat,label_index,axis=1)
        #print(dat[:,1:]) # list operation
        print(dat)
        #print(type(dat[0]))
        return dat#,labels












    def _locate_attr_pos(self,attr_list,case_insensitive=True):
        """
        locate position of attributes according to their str value
        notice: default case insensitive comparison

        :param attr_list:
        :return:
        """
        new_attr_list = cp.deepcopy(self._raw_attribute)

        if case_insensitive: new_attr_list = [item.lower() for item in new_attr_list]

        index_list = [new_attr_list.index(item.lower()) for item in attr_list]

        return index_list


    def _is_number(self,str):
        try:
            float(str)
            return float(str)
        except ValueError:
            pass


if __name__ == "__main__":

    data_array = list()
    data_array.append([1, 'apple',3.6,2,'Alice'])
    data_array.append([0.5, 'cat_walk',4.3,6.7,'Peter'])
    data_array.append([32,'apple',-2,10,'Alice'])

    attr_list = ['value', 'kind','size','price','owner']

    a = DataSet(data_array,attr_list)
    numerical_data_array = a.add_attributes()
    a.setup_data(numerical_data_array)
    print(type(a.dataMatrix[0]))
    #print(a.attributes)
    #print(a.attributes['value'].name,a.attributes['kind'].is_numerical)

    label_attr_list = ['kind','owner']
    #a._generate_labels(label_attr_list)
    #print(a.dataMatrix)
    dat = a.generate_data_partition(label_attr_list)
    #print('data\n',dat)
    #print('labels\n',labels)





























