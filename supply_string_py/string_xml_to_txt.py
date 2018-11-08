# xml 分别输出 key 和 value 文件

import  xlrd

path='/Users/hehongqing/Downloads/test_string.xlsx'
# xlrd.open_workbook(path)

#打开excel文件
data=xlrd.open_workbook(path)     
#获取第一张工作表（通过索引的方式）
table=data.sheets()[0] 
# 获取 sheet name
sheetsNanme=table.name
print('工作表名称'+sheetsNanme)
#data_list用来存放数据
data_list=[]    
#将table中第一行的数据读取并添加到data_list中
data_list.extend(table.row_values(0))
#打印出第一行的全部数据
print('第一行中的各个元素：')
for item in data_list:
    print(item)


