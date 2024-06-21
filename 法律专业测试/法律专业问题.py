# %%
import json
# 定义文件路径
file_path1 = '/法律专业测试/测试数据/法律测试-120-zh.json'
# %%
# 读取第一个JSON文件到列表
with open(file_path1, 'r', encoding='utf-8') as file:
    list1 = json.load(file)

print(len(list1))