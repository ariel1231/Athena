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

class DataPoint(np.matrix):
    """
    a data point consists of id and value list.
    subclassing from numpy.ndarray for further calculation

    """

    def __new__(cls, data_array, data_id=-1, attribute_list = None):
        """
        use __new__ because we need to initiate a datapoint object instead
        of a simple nd-array.

        :param data_array:
        :param attribute_list:
        :return: datapoint object
        """
        #print('cls in __new__:',cls)
        #print("__new__ is called.")
        if len(attribute_list) == len(data_array):
            obj = np.asmatrix(data_array).view(cls)
            #obj.attribute_list = attribute_list
            obj.id = data_id
            obj.info = dict(zip(attribute_list,data_array))
            obj.experiment_label = None
            #print(type(obj))
            return(obj)
        else:
            raise ValueError("The length of the attribute list does not match "
                             "the length of data array.")


    def __array_finalize__(self,obj):
        """
        This is for multiple construction of DataPoint item.
        Please refer to numpy ndarray subclassing webpage for more information.

        :param obj:
        :return:
        """
        #TODO: More advanced attributes such as passing label information

        if obj is None: return
        #self.attribute_list = getattr(obj,'attribute_list',None)
       # print('object type is :',type(obj))
        self.id = getattr(obj,'id',None)
        self.info = getattr(obj,'info',None)
        self.experiment_label = getattr(obj,'experiment_label',None)
        #TODO: change to matrix, make it more clear















if __name__ == "__main__":
    simpleArray = np.array(
        [1,2,3,0,6],

    )
    attributes = ['num_animal','num_fruits','num_vegs','a','b']
    a = DataPoint(simpleArray,'ask_231',attributes) # explicit constructor
    print(a)
    print(a.info)
    print(a.id)

    #print(a, type(a))
    #print(a.attribute_list)
    #print(a[a>2])
    #a[2] = 10
    #print(a)
    #print(isinstance(a,np.ndarray))
    #print(a.id)


    b = a[0,1:] #casting
    print("b: ", b ,  type(b))
    print("Is a and b the same item?",a is b)
    print(b.id)
    print(b.info)
    b.experiment_label = 'abc'
    print(b.experiment_label)

    simpleArray2 = np.array(
        [1, 2, 3, 0, 6],

    )
    second = DataPoint(simpleArray2, 'jkf_231', attributes)  # explicit constructor
    c = second[0,:-1]
    print(c,c.id,'\n')

    d = b+c
    print(d,type(d),d.id)

    e = np.vstack((b,c))
    print(e)
    print('here',type(e[0]),e[0].id)
    #print(b.attribute_list)




