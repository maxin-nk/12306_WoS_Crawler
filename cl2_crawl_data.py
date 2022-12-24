import os
import pandas as pd
# 实现把文件合并的操作
filelist = []

for root, dirs, files in os.walk(r"C:\Users\dell\Downloads\cll", topdown=False):
    for name in files:
        str = os.path.join(root, name)
        if str.split('.')[-1] == 'xls':
            filelist.append(str)

print(filelist)
file1 = pd.read_excel(filelist[0])
# 导入文件
for each_file in  filelist:
    file2 = pd.read_excel(each_file)
    file1 = pd.concat([file1, file2])


file_final = file1.drop_duplicates(subset=['Authors', 'Article Title'], keep='first')
file_final.to_excel(r"C:\Users\dell\Downloads\cll\file_final.xls")
print('finished')