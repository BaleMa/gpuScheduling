import numpy
import os
import scipy
from pynvml import *
from io import StringIO
import re


GPUNUM = 4

#a=numpy.mat('1 2; 3 4',dtype=float)

#getMartix(a)

###print (a.dtype)
'''
try:
    f = open('test.txt','r')
    print(f.read())
    f.close()
except IOError as e:
    print ('excepting:',e)

print (os.uname())
'''
#nvml get device account
'''
nvmlInit()
deviceCount = nvmlDeviceGetCount()
nvmlSystemGetNVMLVersion()

print (deviceCount)


'''



# ~ #----------------------------------------------------------------------
def str2num(LineString, comment='#'):
    """
    #~ >>>NumArray=str2num(LineString,comment='#')
    #~ 将字符串中的所有非Double类型的字符全部替换成空格
    #~ 以'#'开头注释直至行尾,都被清空
    #~ 返回一维numpy.array数组
    """


    NumArray = numpy.empty([0], numpy.float64)
    NumStr = LineString.strip()
    # ~ ignore comment string
    for cmt in comment:
        CmtRe = cmt + '.*$'
        NumStr = re.sub(CmtRe, " ", NumStr.strip(), count=0, flags=re.IGNORECASE)

    # ~ delete all non-number characters,replaced by blankspace.
    NumStr = re.sub('[^0-9.e+-]', " ", NumStr, count=0, flags=re.IGNORECASE)

    # ~ Remove incorrect combining-characters for double type.
    NumStr = re.sub('[.e+-](?=\s)', " ", NumStr.strip(), count=0, flags=re.IGNORECASE)
    NumStr = re.sub('[.e+-](?=\s)', " ", NumStr.strip(), count=0, flags=re.IGNORECASE)
    NumStr = re.sub('[e+-]$', " ", NumStr.strip(), count=0, flags=re.IGNORECASE)
    NumStr = re.sub('[e+-]$', " ", NumStr.strip(), count=0, flags=re.IGNORECASE)

    if len(NumStr.strip()) > 0:
        StrIOds = StringIO(NumStr.strip())
        NumArray = numpy.genfromtxt(StrIOds)
    NumArray = numpy.delete(NumArray,0)
    return NumArray


def file2list(Filename, comment='#', SkipHeadLine=0):
    """
    #~  >>>NumList=file2list(Filename,comment='#',SkipHeadLine=0)
    #~  使用换行符分割字符串
    #~  将字符串中的所有非Double类型的字符全部替换成空格
    #~  以'#'开头注释直至行尾,都被清空
    #~  忽略文件头所有的行数：SkipHeadLine
    #~  将每一行转换成numpy.array数组
    #~  返回numpy.array数组的列表
    #~  注意:每一行的数组中的元素个数可以不一样
    """


    file = open(Filename, 'r')
    String = file.read()
    file.close()

    NumList = []
    StringList = String.split('\n')  # 使用换行符分割字符串
    LineNum = 0
    for Line in StringList:
        LineNum = LineNum + 1
        if (LineNum > SkipHeadLine):
            NumArray = str2num(Line, comment)
            if len(NumArray) > 0:
                NumList.append(NumArray)

    return NumList


def dlmread(Filename, comment='#', dtype=numpy.float64, SkipHeadLine=0):
    """
    #~  Load Data From Txt-File.
    #~  >>>NumpyArray= dlmread(Filename,comment='#',dtype=numpy.float64,SkipHeadLine=0)
    #~  分隔符默认是:";",",",空格类 (包括\t)等等
    #~  以#等开头的被认为是注释,不会被读取
    #~  忽略文件头所有的行数：SkipHeadLine
    #~  Return Value:二维数值数组(numpy.ndarray)
    #~  对文本中数据的排列格式要求最低,且容许出现注释字符,智能化程度最高,但速度较慢
    #~  示例：
    #~  直接读取文件，默认以#等开头的被认为是注释,不会被读取
    #~ >>> x=dlmread(Filename)
    #~  以#！等开头的被认为是注释,不会被读取
    #~ >>> x=dlmread(Filename,comment='#!')
    #~  直接读取文件，指定读取类型
    """

    NumList = file2list(Filename, comment='#', SkipHeadLine=SkipHeadLine)
    # ~ 判断NumList是否为空
    if (len(NumList) > 0):
        dlsize = []  # 每一行数组的大小
        for dL in NumList:
            dlsize.append(dL.size)
            # ~ 判断dlsize的列数
        MinColumnSize = min(dlsize)  # 数组的最大列数
        MaxColumnSize = max(dlsize)  # 数组的最小列数
        # ~ 数组创建和赋值
        NumpyArray = numpy.empty([len(NumList), MinColumnSize], dtype=dtype)

        row = range(0, len(NumList))
        colum = range(0, MinColumnSize)

        for i in row:
            for j in colum:
                NumpyArray[i][j] = NumList[i][j]
    else:
        NumpyArray = []

    return NumpyArray

def file2martix(filename):
    with open(filename, 'r') as f:

        s = f.read()
        martix = dlmread('test.txt',comment='#',dtype=numpy.float64,SkipHeadLine=1)
        return martix
        #while True:
            #s = f.readline()

        '''
            if s :
                list = str2num(s)
                print (list)
            else:
                break
        '''


