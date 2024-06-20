# %%
import json

# 定义文件路径
file_path1 = 'CrimeKgAssitant清洗后_52k_处理后.json'
file_path2 = 'laywer_data.json'
output_file_path = 'self_and_laywer_data.json'

# %%
# 读取第一个JSON文件到列表
with open(file_path1, 'r', encoding='utf-8') as file:
    list1 = json.load(file)

print(len(list1))
# %%
# 读取第二个JSON文件到列表
with open(file_path2, 'r', encoding='utf-8') as file:
    list2 = json.load(file)

print(len(list2))
# 合并两个列表
# %%
merged_list = list2 + list1 + list2
print(len(merged_list))
# 将最终的列表写入一个新的JSON文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(merged_list, file, ensure_ascii=False, indent=4)