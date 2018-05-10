import numpy

class GpuInfo(object):
    def __init__(self, GPUType):
        self.__GPUType = GPUType


    def get_GPUType(self):
        return self.__GPUType
    def __set__(self, GpuType):
        self.__GPUType = GpuType

class Cluster(object):
    def __init__(self, num, martix):
        self.GPUNum = num
        self.GPUS = numpy.arange(0,num,1,dtype=int)
        self.GPUMartix = martix
#numpy.zeros(num, dtype=float)

