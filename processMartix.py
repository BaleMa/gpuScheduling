import numpy
import getMartix
import itertools

#总结矩阵遍历是最好不要写成[][]的形式,合成写与拆开写不一致
#应写成[,]
'''
def PreProcessMatrix(martix, n):
    count = 0
    for i in n:
        for j in n:
            if(martix[i,j]):
                count+=count
'''




def PreProcessMatrix(martix, n):
    Newmartix = numpy.zeros((n,n))
    for i in n:
        for j in n:
            if (martix(i,j) == 'PIX'):
                Newmartix = 1
            elif(martix(i,j) == 'PXB'):
                Newmartix = 1
            elif()(martix(i,j) == 'X'):
                Newmartix = 1

    return Newmartix
'''
numpy.mat(
'X 	PIX	PXB	PXB \
PIX	 X 	PXB	PXB	 \
PXB	PXB	 X 	PIX	 \
PXB	PXB	PIX	 X 	'
)

'''

#获取文件中的矩阵

GPUNUM = 4

martix = getMartix.file2martix('test.txt')
print (martix)

#需要添加错误处理
requestGPUNumber = input()
requestGPUNumber = int(requestGPUNumber)

#如果需求的GPU超过现有的数目，提示数目不够

gpuArray = numpy.arange(GPUNUM).reshape(GPUNUM)

#选出组合数

if requestGPUNumber > GPUNUM:
    print('sorry, there is no so many GPUS')
else:
    #２元及以上
    sumofBandWidth = 0
    weizhi = tuple()
    mutiple = list(itertools.combinations(gpuArray, requestGPUNumber))
    for i in mutiple:
        double = list(itertools.combinations(i, 2))
        temp = 0
        for j in double:
            temp = +martix[j[0],j[1]]
            if temp > sumofBandWidth:
                weizhi = i


    print(weizhi)

