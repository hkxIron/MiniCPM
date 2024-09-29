import os
import shutil
import json

input_dir = "data/AdvertiseGen"
output_dir = "data/AdvertiseGenChatML"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

for fn in ["train.json", "dev.json"]:
    data_out_list = []
    with open(os.path.join(input_dir, fn), "r") as f, open(os.path.join(output_dir, fn), "w") as fo:
        for line in f:
            if len(line.strip()) > 0:
                data = json.loads(line)
                data_out = {'prompt':"请为以下关键词生成一条广告语。\n", "input":data['content'],'output':data['summary']}
                data_out_list.append(data_out)

        for d in data_out_list:
            json_str = json.dumps(d,ensure_ascii=False)  # 将字典转换为JSON字符串
            fo.write(json_str + '\n')  # 写入字符串并添加换行符