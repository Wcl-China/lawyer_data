# %%
import json

# %%
# 打开JSON文件并读取数据
with open('训练数据_带法律依据_92k.json', 'r', encoding='utf-8') as file:
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
    # 提取'answer'作为'instruction'
    instruction = item["answer"]

    # 'input'设置为空字符串
    input_value = ""

    # 将'reference'中的所有字符串合并，并添加'answer'到输出结果
    output_parts = [item["answer"]] +["法律依据如下："] +item["reference"]
    output = " ".join(output_parts)

    # 创建新字典，按照新的格式设置键和值
    new_item = {
        "instruction": instruction,
        "input": input_value,
        "output": output
    }

    # 将新字典添加到新列表中
    new_data_list.append(new_item)


# 计算分割点
split_index_1 = 30000
split_index_2 = split_index_1 + 30000

# 分割列表
data_list_part_1 = new_data_list[:split_index_1]
data_list_part_2 = new_data_list[split_index_1:split_index_2]
data_list_part_3 = new_data_list[split_index_2:]

# 分别导出为JSON文件
def export_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 导出第一部分
export_json(data_list_part_1, '训练数据_带法律依据_92k_处理后_1.json')

# 导出第二部分
export_json(data_list_part_2, '训练数据_带法律依据_92k_处理后_2.json')

# 导出第三部分
export_json(data_list_part_3, '训练数据_带法律依据_92k_处理后_3.json')

print("数据已分为三部分并导出为JSON文件。")