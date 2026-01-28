import pandas as pd #引入pandas包

# 创建一个DataFrom 是一个二维数组
data = {'name':['anna','tim','jek'],'Age':[12,2,45]}
dt_from = pd.DataFrame(data)
print(dt_from)

print()
# Series 是一个一维数组 创建两个series 就可以组成一个DataFrom
series_apples = pd.Series([1,2,3,4,5])
print(series_apples)
series_sun = pd.Series([5,4,3,2,1])
# 将两个series相加 指定列名 得到datafrom
data_from = pd.DataFrame({'sum':series_apples,'sum1':series_sun})
print(data_from)


student = {
    'name':['king','tim','jek'],
    'age':[12,43,11]
}
print(pd.DataFrame(student))