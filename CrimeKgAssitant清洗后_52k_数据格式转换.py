# %%
import json

# %%
# 打开JSON文件并读取数据
with open('CrimeKgAssitant清洗后_52k.json', 'r', encoding='utf-8') as file:
    # 使用json.load()解析JSON文件
    data_list = json.load(file)

# 检查解析后的数据类型
print(type(data_list))  # 输出应为<class 'list'>
# %%
print(len(data_list))

# %%
# 创建新的列表，用于存储转换后的数据
new_data_list = []

# 遍历原始列表中的每个元素
for item in data_list:
    # 创建新字典，按照新的格式设置键和值
    new_item = {
        "instruction": item["input"],  # 将'input'的值复制为'instruction'
        "input": "",  # 新格式中'input'的值为空字符串
        "output": item["output"]  # 'output'的值保持不变
    }
    # 将新字典添加到新列表中
    new_data_list.append(new_item)

# 将新列表转换为JSON格式的字符串
new_json_str = json.dumps(new_data_list, ensure_ascii=False, indent=2)

# 将JSON格式的字符串写入文件
with open('CrimeKgAssitant清洗后_52k_处理后.json', 'w', encoding='utf-8') as file:
    file.write(new_json_str)

print("转换完成并已写入 new_format.json 文件。")